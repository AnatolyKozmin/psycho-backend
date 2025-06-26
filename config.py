import os 
from typing import List, Optional

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pydantic_settings import BaseSettings

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

class Settings(BaseSettings):
    BOT_TOKEN: Optional[str] = os.getenv('BOT_TOKEN')
    FORMAT_LOG: str = "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}"
    LOG_ROTATION: str = "10 MB"
    DB_URL: str = 'postgresql+asyncpg://psycho:1234@localhost:5432/psycho_db'
    JOB_STORE_URL: str = 'postgresql://psycho:1234@localhost:5432/psycho_db'
    BASE_SITE: str
    TG_API_SITE: str
    FRONT_SITE: str

    def get_webhook_url(self) -> str:
        return f"{self.BASE_SITE}/webhook"
    
    def get_tg_api_url(self) -> str: 
        return f"{self.TG_API_SITE}/bot{self.BOT_TOKEN}"
    

settings = Settings()
database_url = settings.DB_URL 
scheduler = AsyncIOScheduler(jobstores={'default': SQLAlchemyJobStore(url=settings.JOB_STORE_URL)})