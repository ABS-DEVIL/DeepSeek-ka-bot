import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Telegram
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    BOT_NAME = "ABS_Stream_Fucker"
    
    # MongoDB
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    DB_NAME = "stream_fucker_db"
    
    # Admin
    ADMINS = [int(id) for id in os.getenv("ADMINS", "").split(",")]
    
    # User Limits
    FREE_DAILY_FILES = 4
    FREE_DAILY_LINKS = 5
    FREE_WAIT_TIME = 8
    PREMIUM_WAIT_TIME = 0
    
    # Expiry
    TOKEN_EXPIRY_FREE = 24 * 3600  # 24 hours
    TOKEN_EXPIRY_PREMIUM = 30 * 24 * 3600  # 30 days
    
    # Web
    WEB_HOST = "0.0.0.0"
    WEB_PORT = 8000
    DOMAIN = os.getenv("DOMAIN", "https://your-domain.com")
    
    # Security
    SECRET_KEY = os.getenv("SECRET_KEY")
    
    # Force Subscribe
    FSUB_CHANNELS = [
        {"id": -1001234567890, "name": "Main Channel", "url": "https://t.me/..."},
    ]

config = Config()
