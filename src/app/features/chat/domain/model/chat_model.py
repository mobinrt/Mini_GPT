from tortoise import fields

from src.app.features.message.domain.model.message_model import MessageModel
from src.app.core.config.model.base_model import BaseModel
from src.app.core.websocket.websocket_model import WebSocketSession
from src.app.features.share_link.domain.model.link_model import LinkModel

class ChatModel(BaseModel):
    project_id = fields.ForeignKeyField('models.ProjectModel', related_name='chats', on_delete=fields.CASCADE)
    
    title = fields.CharField(max_length=50)
    is_active = fields.BooleanField(default=False)
    last_active = fields.DatetimeField(null=True)
    
    messages = fields.ReverseRelation['MessageModel']
    
    class Meta:
        table = 'chats'
        indexes = [("project_id",)]
    
