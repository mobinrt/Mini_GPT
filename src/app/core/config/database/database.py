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


db = Database() 
