from tortoise import fields
from tortoise.validators import RegexValidator

from src.app.core.websocket.websocket_model import WebSocketSession
from src.app.core.config.model.base_model import BaseModel
from src.app.features.project.domain.model.project_model import ProjectModel
from src.app.features.share_link.domain.model.link_model import LinkModel

class UserModel(BaseModel):
    id = fields.UUIDField(primary_key=True)
    username = fields.CharField(max_length=50)
    email = fields.CharField(   
                            max_length=100, 
                            unique=True,
                            validators=[
                                RegexValidator(
                                regex=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
                                message='Invalid email address format.'
                                    )
                                ],
                            )
    password_hash = fields.CharField(max_length=200)
    is_admin = fields.BooleanField(default=False)
    is_premium = fields.BooleanField(default=False)
    pic_url = fields.CharField(max_length=255, null=True)
    
    projects = fields.ReverseRelation['ProjectModel']
    share_links = fields.ReverseRelation['LinkModel']
    websocket_session = fields.ReverseRelation["WebSocketSession"]
    links = fields.ReverseRelation['LinkModel']
    
    class Meta:
        table = 'users'