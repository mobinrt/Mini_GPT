from tortoise import fields

from src.app.features.message.domain.model.message_model import MessageModel

class PromptModel(MessageModel):
    
    class Meta:
        table = 'prompts'
