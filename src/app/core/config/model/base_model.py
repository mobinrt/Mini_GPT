from tortoise import fields
from tortoise.models import Model

class BaseModel(Model):
    id = fields.IntField(primary_key=True) 
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    updated_at = fields.DatetimeField(null=True, auto_now=True)
    
    class Meta:
        abstract = True
