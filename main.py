from fastapi import FastAPI, HTTPException, status
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise
import uvicorn
from fastapi.responses import JSONResponse

from src.app.core.config.database import TORTOISE_ORM  
from src.app.features.user.router.user_routers import user_router
from src.app.features.user.admin.router.admin_routers import admin_router
from src.app.features.user.auth.api.auth_rout import router
from src.app.core.exception.auth_exceptions import AccessDenied


async def lifespan(app: FastAPI):
    print("Initializing database...")
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas() 
    yield 
    print("Closing database connection...")
    await Tortoise.close_connections()

app = FastAPI(lifespan=lifespan)


register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True, 
    add_exception_handlers=True,
)

app.include_router(user_router)
app.include_router(admin_router)
app.include_router(router)

@app.get('/')
def start():
    return 'this is my GPT project!!'
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


@app.exception_handler(AccessDenied)
async def base_error_handler(request, exc: AccessDenied):
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={"detail": str(exc)}, 
    )

       
    
