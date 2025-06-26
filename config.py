import os
from typing import Optional

class Config:
    """Configuration class for the Schedule API"""
    
    # External API configuration
    EXTERNAL_API_URL: str = os.getenv(
        "EXTERNAL_API_URL", 
        "https://test.lumeneo.ai/services/appointment/api/appointments"
    )
    
    # API configuration
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))
    
    # HTTP client configuration
    REQUEST_TIMEOUT: int = int(os.getenv("REQUEST_TIMEOUT", "30"))
    
    # Logging configuration
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    # Optional authentication headers for external API
    EXTERNAL_API_KEY: Optional[str] = os.getenv("EXTERNAL_API_KEY")
    EXTERNAL_API_SECRET: Optional[str] = os.getenv("EXTERNAL_API_SECRET")

# Global config instance
config = Config() 