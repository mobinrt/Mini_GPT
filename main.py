from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise
import uvicorn
 
from src.app.core.config.database import TORTOISE_ORM  
from src.app.features.user.router.user_routers import user_router


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

@app.get('/')
def start():
    return 'this is my university project!!'
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
