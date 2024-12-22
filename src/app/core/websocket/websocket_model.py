from tortoise import fields
from tortoise.models import Model

class WebSocketSession(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="sessions", on_delete=fields.CASCADE)
    chat = fields.ForeignKeyField("models.Chat", related_name="sessions", on_delete=fields.CASCADE)
    connected_at = fields.DatetimeField(auto_now_add=True)
    disconnected_at = fields.DatetimeField(null=True)

    class Meta:
        table = "websocket_sessions"