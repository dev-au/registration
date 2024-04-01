from routes import main_router
from config.auth import *
from config.schemas import *


@main_router.post("/getme")
async def signup_user(current_user: User = Depends(get_current_user)):
    return current_user
