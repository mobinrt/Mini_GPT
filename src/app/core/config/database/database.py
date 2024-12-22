from tortoise import Tortoise, fields
from tortoise.models import Model
from typing import AsyncGenerator

from src.app.core.config.setting import Settings

class Database:
    DATABASE_URL = Settings.database_url
    
    def __init__(self):
        self.db_config = {
            'connections': {'default': self.DATABASE_URL},
            'apps': {
                'models': {
                    'models': [
                        'src.app.core.config.model.base_model',
                        'src.app.features.user.domain.model.user_model',
                        'src.app.features.project.domain.model.project_model',
                        'src.app.features.chat.domain.model.chat_model',
                        'src.app.features.message.domain.model.message_model',
                        'src.app.features.message.domain.model.responce_model',
                        'src.app.features.message.domain.model.prompt_model',
                        'src.app.features.share_link.domain.model.link_model',
                        'src.app.core.websocket.websocket_model',
                        'aerich.models' 
                    ],
                    'default_connection': 'default'
                },
            },
        }
        
    async def init_db(self):
        await Tortoise.init(self.db_config)
        await Tortoise.generate_schemas()

    async def get_session(self) -> AsyncGenerator:
        async with Tortoise.get_connection("default").acquire() as connection:
            yield connection

db = Database()