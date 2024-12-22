from tortoise import fields

from src.app.core.config.model.base_model import BaseModel
from src.app.features.chat.domain.model.chat_model import ChatModel
from src.app.features.share_link.domain.model.link_model import LinkModel

class ProjectModel(BaseModel):
    owner_id = fields.ForeignKeyField('models.UserModel', related_name='projects', on_delete=fields.CASCADE)
    
    name = fields.CharField(max_lenght=50)
    description = fields.CharField(max_lenght=100)
    
    chats = fields.ReverseRelation['ChatModel']
    links = fields.ReverseRelation['LinkModel']
    
    class Meta:
        table = 'projects'