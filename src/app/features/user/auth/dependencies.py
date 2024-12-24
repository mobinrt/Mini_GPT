from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from .service.auth_service_imp import AuthServiceImp
from src.core.config.database.database import db
from ..domain.model.user_model import UserModel

async def get_auth_service(db_session: AsyncSession = Depends(db.get_session)) -> AuthServiceImp:
    return AuthServiceImp(session=db_session, model=UserModel)

