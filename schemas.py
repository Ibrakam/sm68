from pydantic import BaseModel
from typing import Optional



class UserSchema(BaseModel):
    name: str
    surname: Optional[str] = None
    username: str
    password: str
    phone_number: str
    email: str
    date_of_birth: Optional[str] = None



