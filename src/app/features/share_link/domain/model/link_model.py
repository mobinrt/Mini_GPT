from tortoise import fields
from datetime import datetime, timedelta

from src.app.core.config.model.base_model import BaseModel
from src.app.features.project.domain.model.project_model import ProjectModel

class LinkModel(BaseModel):
    project_id = fields.ForeignKeyField('models.ProjectModel', related_name='links', on_delete=fields.CASCADE)
    chat_id = fields.ForeignKeyField("models.ChatModel", related_name='links', on_delete=fields.CASCADE)
    user_id = fields.ForeignKeyField("models.UserModel", related_name='links', on_delete=fields.CASCADE)
    
    link_url = fields.CharField(max_length=255, null=True)
    is_public = fields.BooleanField(default=False)
    
    class Meta:
        table = 'links'
        
    @property
    def expired_at(self) -> datetime:
        if self.created_at:
            return self.created_at + timedelta(hours=24)
        return None