from tortoise import fields

from src.app.core.config.model.base_model import BaseModel
from src.app.core.enum.message_status import MessageStatus

class MessageModel(BaseModel):    
    chat_id = fields.ForeignKeyField("models.ChatModel", on_delete=fields.CASCADE)

    content = fields.TextField()
    status = fields.CharEnumField(enum_type=MessageStatus, default=MessageStatus.SENT.value)
    
    class Meta:
        abstract = True