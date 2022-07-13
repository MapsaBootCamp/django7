from typing import Union
from pydantic import BaseModel



class User(BaseModel):
    username: str
    firstname: Union[str, None] = None
    lastname: Union[str, None] = None


class UserInDB(User):
    password: str