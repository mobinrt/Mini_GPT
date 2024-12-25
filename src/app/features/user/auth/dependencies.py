from src.app.features.user.auth.service.auth_service_imp import AuthServiceImp
from src.app.features.user.domain.model.user_model import UserModel

async def get_auth_service() -> AuthServiceImp:
    return AuthServiceImp(model=UserModel)
