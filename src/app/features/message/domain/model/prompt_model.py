from tortoise import fields

from src.app.features.message.domain.model.message_model import MessageModel
from src.app.features.message.domain.model.responce_model import ResponceModel

class PromptModel(MessageModel):
    responces = fields.ReverseRelation['ResponceModel']
    
    class Meta:
        table = 'prompts'
