from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from . import schema
from . import controller

router = APIRouter(prefix="/api/auth")

oAuth2Bearer = OAuth2PasswordBearer(tokenUrl="sign_in")


@router.get("/token", status_code=status.HTTP_200_OK, response_model=schema.User)
async def get_current_user(token: str = Depends(oAuth2Bearer)) -> dict:
    user: dict = controller.verify_token(token)
    return user


@router.post("/sign-in", response_model=schema.Token, status_code=status.HTTP_200_OK)
async def sign_in(data: schema.SignInRequest):
    user: dict = controller.authenticate_user(data)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid Username or (section_code, Unique Registration Number)...")
    access_token: str = controller.create_token(user.get("id"))
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/sign-up", status_code=status.HTTP_201_CREATED, response_model=schema.Token)
async def sign_up(data: schema.SignUpRequest):
    if controller.check_user_exits(data.username):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already registered")
    user: dict = controller.create_user(data.dict())
    access_token: str = controller.create_token(user.get("id"))
    return {"access_token": access_token, "token_type": "bearer"}
