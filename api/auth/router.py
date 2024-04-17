from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordBearer
from lib import token as a_utils

from . import schema
from database.database import AuthDB as DB

router = APIRouter(prefix="/api/auth")

oAuth2Bearer = OAuth2PasswordBearer(tokenUrl="sign_in")


def authenticate_user(data: schema.Auth) -> dict:
    user: dict = DB.get_user_by_username(data.username)
    if user:
        if data.section_code == user.get("section_code") or data.unique_registration_number == user.get(
                "unique_registration_number"):
            return user
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Invalid Username or (section_code, Unique Registration Number)...")


@router.get("/token", status_code=status.HTTP_200_OK, response_model=schema.User)
async def get_current_user(token: str = Depends(oAuth2Bearer)) -> dict:
    user_id: str = a_utils.verify_access_token(token)
    user: dict = DB.get_user_by_id(user_id)
    return user


@router.post("/sign-in", response_model=schema.Token, status_code=status.HTTP_200_OK)
async def sign_in(data: schema.SignInRequest):
    user: dict = authenticate_user(data)
    access_token: str = a_utils.create_access_token(data={"sub": user.get("id")})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/sign-up", status_code=status.HTTP_201_CREATED, response_model=schema.Token)
async def sign_up(data: schema.SignUpRequest):
    user: dict = DB.get_user_by_username(data.username)
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already registered")
    user: dict = DB.create_user(data.dict())
    access_token: str = a_utils.create_access_token(data={"sub": user.get("id")})
    return {"access_token": access_token, "token_type": "bearer"}
