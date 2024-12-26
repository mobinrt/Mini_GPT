from fastapi import APIRouter

from .get_admin_api import router as get_admin_api

admin_router = APIRouter()

admin_router.include_router(get_admin_api)
