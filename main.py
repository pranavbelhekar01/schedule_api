from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import httpx
import json
from datetime import datetime
from config import config
import os

app = FastAPI(title="Schedule API", description="API to restructure and forward appointment data")

# Input model for the original format
class AppointmentInput(BaseModel):
    site_id: int
    title: str
    start_time: str
    end_time: str
    license_plate_1: str
    description: str
    customer_id: int
    customer_name: str
    customer_email: str
    customer_mobile: str
    work_order_id: int

# Output model for the restructured format
class Participant(BaseModel):
    customer_id: int
    name: str
    email: str
    mobile: str

class AppointmentOutput(BaseModel):
    site_id: int
    title: str
    start_time: str
    end_time: str
    license_plates: List[str]
    description: str
    participants: List[Participant]
    work_order_id: int

@app.post("/restructure-appointment", response_model=dict)
async def restructure_appointment(appointment_data: AppointmentInput):
    """
    Restructure appointment data and forward to external API
    """
    try:
        # Restructure the data
        restructured_data = {
            "site_id": appointment_data.site_id,
            "title": appointment_data.title,
            "start_time": appointment_data.start_time,
            "end_time": appointment_data.end_time,
            "license_plates": [appointment_data.license_plate_1],
            "description": appointment_data.description,
            "participants": [
                {
                    "customer_id": appointment_data.customer_id,
                    "name": appointment_data.customer_name,
                    "email": appointment_data.customer_email,
                    "mobile": appointment_data.customer_mobile
                }
            ],
            "work_order_id": appointment_data.work_order_id
        }
        
        # Prepare headers for external API (no authentication needed)
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        # Forward to external API
        async with httpx.AsyncClient() as client:
            response = await client.post(
                config.EXTERNAL_API_URL,
                json=restructured_data,
                headers=headers,
                timeout=config.REQUEST_TIMEOUT
            )
            
            # Check if the request was successful
            response.raise_for_status()
            
            # Return the response from the external API
            return response.json()
            
    except httpx.HTTPStatusError as e:
        # Handle HTTP errors from the external API
        error_detail = f"External API error: {e.response.status_code} - {e.response.text}"
        raise HTTPException(status_code=e.response.status_code, detail=error_detail)
        
    except httpx.RequestError as e:
        # Handle network/connection errors
        error_detail = f"Network error: {str(e)}"
        raise HTTPException(status_code=503, detail=error_detail)
        
    except Exception as e:
        # Handle any other unexpected errors
        error_detail = f"Internal server error: {str(e)}"
        raise HTTPException(status_code=500, detail=error_detail)

@app.get("/")
async def root():
    """
    Root endpoint with API information
    """
    return {
        "message": "Schedule API - Appointment Restructuring Service",
        "version": "1.0.0",
        "endpoints": {
            "POST /restructure-appointment": "Restructure and forward appointment data"
        },
        "external_api": config.EXTERNAL_API_URL,
        "deployment": "Render"
    }

@app.get("/health")
async def health_check():
    """
    Health check endpoint
    """
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}

if __name__ == "__main__":
    import uvicorn
    # Get port from environment variable (for Render) or use default
    port = int(os.getenv("PORT", config.API_PORT))
    uvicorn.run(app, host=config.API_HOST, port=port) 