from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    phone: str


class CreateUser(UserBase):
    password: str
