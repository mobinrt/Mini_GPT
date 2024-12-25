from tortoise import fields

from src.app.features.message.domain.model.message_model import MessageModel
from src.app.core.enum.responce_status import ResponceStatus

class ResponceModel(MessageModel):
    prompt_id = fields.ForeignKeyField('models.PromptModel', related_name='responces', on_delete=fields.CASCADE)
    like_status = fields.CharEnumField(enum_type=ResponceStatus, default=ResponceStatus.NONE.value)
    
    class Meta:
        table = 'responces'
        indexes = [("prompt_id",)]