from tortoise import fields

from src.app.core.config.model.base_model import BaseModel

class ProjectModel(BaseModel):
    owner_id = fields.ForeignKeyField('models.UserModel', related_name='projects', on_delete=fields.CASCADE)
    
    name = fields.CharField(max_length=50)
    description = fields.CharField(max_length=100)
     
    class Meta:
        table = 'projects'