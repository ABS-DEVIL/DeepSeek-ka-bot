from datetime import datetime, timedelta
from typing import Optional
from pydantic import BaseModel
from pymongo import MongoClient
from config.settings import config

client = MongoClient(config.MONGO_URI)
db = client[config.DB_NAME]

class User(BaseModel):
    user_id: int
    username: Optional[str]
    is_premium: bool = False
    is_banned: bool = False
    is_muted: bool = False
    muted_until: Optional[datetime]
    daily_files_used: int = 0
    daily_links_used: int = 0
    last_reset: datetime = datetime.utcnow()
    joined_date: datetime = datetime.utcnow()
    
class File(BaseModel):
    file_id: str
    unique_id: str
    user_id: int
    file_name: str
    file_size: int
    mime_type: str
    password: Optional[str] = None
    access_key: Optional[str] = None
    token: str
    token_expiry: datetime
    password_expiry: Optional[datetime]
    is_public: bool = True
    uploaded_at: datetime = datetime.utcnow()
    leech_source: Optional[str] = None
    
class Log(BaseModel):
    log_id: str
    user_id: int
    action: str  # start, upload, generate, stream, download, etc.
    details: dict
    timestamp: datetime = datetime.utcnow()
    
# Collections
users_collection = db["users"]
files_collection = db["files"]
logs_collection = db["logs"]
