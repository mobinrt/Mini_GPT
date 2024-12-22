from tortoise import fields

from src.app.core.config.model.base_model import BaseModel
from src.app.features.project.domain.model.project_model import ProjectModel
from app.features.share_link.domain.model.link_model import LinkModel
from src.app.core.enum.message_status import MessageStatus

class MessageModel(BaseModel):    
    chat_id = fields.ForeignKeyField("models.ChatModel", related_name='messages', on_delete=fields.CASCADE)

    content = fields.TextField()
    status = fields.CharEnumField(choices=MessageStatus, default="S")
    
    class Meta:
        abstract = True