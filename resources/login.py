from routes import main_router
from config.auth import *


@main_router.post("/login")
async def login_for_access_token(form_data: LoginModel):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"user": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

