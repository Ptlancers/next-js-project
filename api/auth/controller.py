from . import schema
from database.database import AuthDB as DB
from lib import token as token_utils


def authenticate_user(data: schema.Auth) -> dict:
    user: dict = DB.get_user_by_username(data.username)
    if user:
        if data.section_code == user.get("section_code") or data.unique_registration_number == user.get(
                "unique_registration_number"):
            return user
    return {}


def verify_token(token: str) -> dict:
    user_id: str = token_utils.verify_access_token(token)
    user: dict = DB.get_user_by_id(user_id)
    return user


def create_token(data: str) -> str:
    access_token: str = token_utils.create_access_token(data={"sub": data})
    return access_token


def check_user_exits(username: str) -> bool:
    user: dict = DB.get_user_by_username(username)
    return bool(user)


def create_user(data: dict) -> dict:
    return DB.create_user(data)
