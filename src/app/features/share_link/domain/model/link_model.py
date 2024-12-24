from tortoise import fields
from datetime import datetime, timedelta

from src.app.core.config.model.base_model import BaseModel

class LinkModel(BaseModel):
    project_id = fields.ForeignKeyField('models.ProjectModel', related_name='links', on_delete=fields.CASCADE, null=True)
    chat_id = fields.ForeignKeyField("models.ChatModel", related_name='links', on_delete=fields.CASCADE, null=True)
    user_id = fields.ForeignKeyField("models.UserModel", related_name='links', on_delete=fields.CASCADE)
    
    link_url = fields.CharField(max_length=255, null=True)
    is_public = fields.BooleanField(default=False)
    
    class Meta:
        table = 'links'
        
    @property
    def expired_at(self) -> datetime:
        if not self.created_at:
            raise ValueError("The 'created_at' field is not set.")
        return self.created_at + timedelta(hours=24)