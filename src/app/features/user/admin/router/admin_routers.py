from fastapi import APIRouter

from .get_user_api import router as get_user_api

user_router = APIRouter()

user_router.include_router(get_user_api)
