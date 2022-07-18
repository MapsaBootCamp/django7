from typing import Union
from pydantic import BaseModel, Field



class User(BaseModel):
    username: str
    firstname: Union[str, None] = None
    lastname: Union[str, None] = None
    age: Union[int, None] = Field(default=None, gt=0)


class UserUpdate(BaseModel):
    firstname: Union[str, None] = None
    lastname: Union[str, None] = None
    age: Union[int, None] = Field(default=None, gt=0)


class UserInDB(User):
    password: str


class UserOut(BaseModel):
    username: str 
    firstname: Union[str, None] = None


class Token(BaseModel):
    access_token: str
    token_type: str