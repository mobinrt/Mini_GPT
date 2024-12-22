from tortoise import fields

from src.app.features.message.domain.model.message_model import MessageModel
from src.app.features.message.domain.model.prompt_model import PromptModel
from src.app.core.enum.responce_status import ResponceStatus

class ResponceModel(MessageModel):
    prompt_id = fields.ForeignKeyField('models.prompt', related_name='responces', on_delete=fields.CASCADE)
    like_status = fields.CharEnumField(choices=ResponceStatus, default="N")
    
    class Meta:
        table = 'responces'