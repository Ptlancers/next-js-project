from pydantic import BaseModel



class Auth(BaseModel):
    username: str
    section_code: str
    unique_registration_number: str


class SignInRequest(Auth):
    pass



class SignUpRequest(Auth):
    date_insurance_of_urn: str

class User(SignUpRequest):
    # id:str
    pass

class Token(BaseModel):
    access_token: str
    token_type: str
