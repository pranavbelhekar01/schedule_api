import os
from typing import Optional

class Config:
    """Configuration class for the Schedule API"""
    
    # External API configuration - hardcoded since no authentication needed
    EXTERNAL_API_URL: str = "https://test.lumeneo.ai/services/appointment/api/appointments"
    
    # API configuration
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    
    # HTTP client configuration
    REQUEST_TIMEOUT: int = 30
    
    # Logging configuration
    LOG_LEVEL: str = "INFO"

# Global config instance
config = Config() 