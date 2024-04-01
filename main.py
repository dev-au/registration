from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from config.data import DB_URL
from routes import main_router
import resources

app = FastAPI()
app.include_router(main_router)

register_tortoise(
    app,
    db_url=DB_URL,
    modules={'models': ['config.models']},
    generate_schemas=True
)
