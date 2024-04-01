from routes import main_router
from config.auth import *
from config.schemas import *


@main_router.post("/signup")
async def signup_user(user: UserModel):
    user_exists = await User.get_or_none(username=user.username)
    if user_exists:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, 'Error! User already created with given username')
    await User.create(username=user.username, fullname=user.fullname, hashed_password=get_password_hash(user.password))
    raise HTTPException(status.HTTP_201_CREATED, 'User created successfully!')
