import requests
import json

# Test data matching the input format
test_data = {
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

def test_api():
    """Test the restructure-appointment endpoint"""
    
    # API endpoint
    url = "http://localhost:8000/restructure-appointment"
    
    print("📤 INPUT DATA (Original Format):")
    print("=" * 50)
    print(json.dumps(test_data, indent=2))
    print()
    
    print("🔄 EXPECTED RESTRUCTURED DATA (Sent to External API):")
    print("=" * 50)
    expected_restructured = {
        "site_id": test_data["site_id"],
        "title": test_data["title"],
        "start_time": test_data["start_time"],
        "end_time": test_data["end_time"],
        "license_plates": [test_data["license_plate_1"]],
        "description": test_data["description"],
        "participants": [
            {
                "customer_id": test_data["customer_id"],
                "name": test_data["customer_name"],
                "email": test_data["customer_email"],
                "mobile": test_data["customer_mobile"]
            }
        ],
        "work_order_id": test_data["work_order_id"]
    }
    print(json.dumps(expected_restructured, indent=2))
    print()
    
    try:
        print("🌐 MAKING REQUEST TO OUR API...")
        print("=" * 50)
        print(f"URL: {url}")
        print(f"Method: POST")
        print(f"Headers: Content-Type: application/json")
        print()
        
        # Make the POST request
        response = requests.post(
            url,
            json=test_data,
            headers={"Content-Type": "application/json"},
            timeout=30
        )
        
        print("📊 RESPONSE DETAILS:")
        print("=" * 50)
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        print()
        
        if response.status_code == 200:
            print("✅ SUCCESS! EXTERNAL API RESPONSE:")
            print("=" * 50)
            response_data = response.json()
            print(json.dumps(response_data, indent=2))
            print()
            
            # Extract key information
            if "appointment_id" in response_data:
                print(f"🎯 Appointment ID: {response_data['appointment_id']}")
            if "time_status" in response_data:
                print(f"⏰ Time Status: {response_data['time_status']}")
            if "progress_status" in response_data:
                print(f"📈 Progress Status: {response_data['progress_status']}")
            if "created_at" in response_data:
                print(f"📅 Created At: {response_data['created_at']}")
                
        else:
            print("❌ ERROR OCCURRED:")
            print("=" * 50)
            print(f"Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ CONNECTION ERROR:")
        print("=" * 50)
        print("Make sure the FastAPI server is running on localhost:8000")
        print("Run: python main.py")
    except requests.exceptions.Timeout:
        print("❌ TIMEOUT ERROR:")
        print("=" * 50)
        print("Request took too long to complete")
    except Exception as e:
        print("❌ UNEXPECTED ERROR:")
        print("=" * 50)
        print(f"Error: {str(e)}")

def test_health_check():
    """Test the health check endpoint"""
    
    url = "http://localhost:8000/health"
    
    print("🏥 HEALTH CHECK:")
    print("=" * 50)
    
    try:
        response = requests.get(url, timeout=10)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            print("✅ Health check passed")
            health_data = response.json()
            print(f"Status: {health_data.get('status', 'unknown')}")
            print(f"Timestamp: {health_data.get('timestamp', 'unknown')}")
        else:
            print("❌ Health check failed")
            
    except Exception as e:
        print(f"❌ Health check error: {str(e)}")
    
    print()

if __name__ == "__main__":
    print("🧪 TESTING SCHEDULE API")
    print("=" * 60)
    print()
    
    # Test health check first
    test_health_check()
    
    # Test the main endpoint
    test_api()
    
    print("=" * 60)
    print("🏁 TEST COMPLETED!")
    print("=" * 60) 