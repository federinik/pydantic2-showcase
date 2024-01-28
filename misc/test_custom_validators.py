from pydantic import BaseModel, validator


class RegistrationForm(BaseModel):
    user: str
    pwd: str
    confirm_pwd: str

    @validator('confirm_pwd')
    def check_pwd_equal(cls, v: str) -> str:

        return v
