import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # JWT 
    SECRET_KEY:str = os.getenv("SECRET_KEY")  
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES:int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    REFRESH_TOKEN_EXPIRE_DAYS:int = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS"))
    
    if not SECRET_KEY or not ALGORITHM:
        raise ValueError("Environment variables SECRET_KEY and ALGORITHM must be set!")

    authjwt_secret_key: str = SECRET_KEY
    authjwt_algorithm: str = ALGORITHM

   
    # db
    DB_USER:str = os.getenv("DB_USER")
    DB_PASSWORD:str = os.getenv("DB_PASSWORD")
    DB_HOST:str = os.getenv("DB_HOST")
    DB_PORT:int  = os.getenv("DB_PORT")
    DB_NAME:str  = os.getenv("DB_NAME")
    
    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

settings = Settings()
