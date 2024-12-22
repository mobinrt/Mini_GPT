from tortoise import fields

from src.app.features.project.domain.model.project_model import ProjectModel
from src.app.features.message.domain.model.message_model import MessageModel
from src.app.core.config.model.base_model import BaseModel
from src.app.core.websocket.websocket_model import WebSocketSession
from src.app.features.share_link.domain.model.link_model import LinkModel

class ChatModel(BaseModel):
    project_id = fields.ForeignKeyField('models.ProjectModel', related_name='chats', on_delete=fields.CASCADE)
    
    title = fields.CharField(max_lenght=50)
    is_active = fields.BooleanField(default=False)
    last_active = fields.DatetimeField(null=True)
    
    messages = fields.ReverseRelation['MessageModel']
    websocket_session = fields.ReverseRelation["WebSocketSession"]
    links = fields.ReverseRelation['LinkModel']
    
    class Meta:
        table = 'chats'
    
