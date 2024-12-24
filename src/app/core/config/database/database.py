from tortoise import Tortoise
from typing import AsyncGenerator
import asyncio  
import os

from src.app.core.config.setting import TORTOISE_ORM
from tortoise import Tortoise

class Database:
    
    def __init__(self):
        self.db_config = TORTOISE_ORM
        
    async def init_db(self):
        await Tortoise.init(self.db_config)
        await Tortoise.generate_schemas()

    async def get_session(self) -> AsyncGenerator:
        async with Tortoise.get_connection("default").acquire() as connection:
            yield connection

db = Database() 
async def a():
    print("DB_USER:", os.getenv("DB_USER"))
    print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
    print("DB_HOST:", os.getenv("DB_HOST"))
    print("DB_PORT:", os.getenv("DB_PORT"))
    print("DB_NAME:", os.getenv("DB_NAME"))
    try:
        await Tortoise.init(config=TORTOISE_ORM)
        print("Database connection successful!")
    except Exception as e:
        print(f"Failed to connect to the database: {e}")
        

if __name__ == "__main__":  
    asyncio.run(a())  