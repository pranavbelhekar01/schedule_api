# Schedule API - Appointment Restructuring Service

This FastAPI application restructures appointment data and forwards it to an external API.

## Features

- Restructures appointment data from flat format to nested format
- Forwards restructured data to external API
- Comprehensive error handling
- Health check endpoint
- Automatic API documentation

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## API Endpoints

### POST /restructure-appointment

Restructures appointment data and forwards it to the external API.

**Input Format:**
```json
{
  "site_id": 10,
  "title": "Car Repair and Wash Appointment",
  "start_time": "2025-06-23T10:00:00Z",
  "end_time": "2025-06-23T11:00:00Z",
  "license_plate_1": "MH 12 DF 8096",
  "description": "Car Repair and Wash Appointment for MH 12 DF 8096",
  "customer_id": 1,
  "customer_name": "Parish",
  "customer_email": "parish@lumeneo.ai",
  "customer_mobile": "+918920626776",
  "work_order_id": 1
}
```

**Output Format (sent to external API):**
```json
{
    "site_id": 10,
    "title": "Car Repair and Wash Appointment",
    "start_time": "2025-06-23T10:00:00Z",
    "end_time": "2025-06-23T11:00:00Z",
    "license_plates": [
        "MH 12 DF 8096"
    ],
    "description": "Car Repair and Wash Appointment for MH 12 DF 8096",
    "participants": [
        {
            "customer_id": 1,
            "name": "Parish",
            "email": "parish@lumeneo.ai",
            "mobile": "+918920626776"
        }
    ],
    "work_order_id": 1
}
```

### GET /

Returns API information and available endpoints.

### GET /health

Health check endpoint.

## API Documentation

Once the server is running, you can access:
- Interactive API documentation: http://localhost:8000/docs
- Alternative API documentation: http://localhost:8000/redoc

## Example Usage

```bash
curl -X POST "http://localhost:8000/restructure-appointment" \
     -H "Content-Type: application/json" \
     -d '{
       "site_id": 10,
       "title": "Car Repair and Wash Appointment",
       "start_time": "2025-06-23T10:00:00Z",
       "end_time": "2025-06-23T11:00:00Z",
       "license_plate_1": "MH 12 DF 8096",
       "description": "Car Repair and Wash Appointment for MH 12 DF 8096",
       "customer_id": 1,
       "customer_name": "Parish",
       "customer_email": "parish@lumeneo.ai",
       "customer_mobile": "+918920626776",
       "work_order_id": 1
     }'
```

## Error Handling

The API includes comprehensive error handling for:
- HTTP errors from the external API
- Network/connection errors
- Internal server errors
- Validation errors

## External API

The restructured data is forwarded to:
`https://test.lumeneo.ai/services/appointment/api/appointments` 