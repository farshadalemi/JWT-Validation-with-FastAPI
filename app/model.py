from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional

class ContactSchema(BaseModel):
    id: int = Field(default=None)
    name: str = Field(default=None)
    phone: str = Field(default=None)  
    email: str = Field(default=None)
    created_at: str = Field(default=None)
    updated_at: str = Field(default=None)
    delete_flag: int = Field(default=None)
    deleted_at: Optional[str] = Field(default=None)


class UserSchema(BaseModel):
    id: int = Field(default=None)
    fullname : str = Field(default=None)
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo" : {
                "id" : 1,
                "name" : "test",
                "email" : "test@test.com",
                "password" : "1111"
            }
        }

class UserLoginSchema(BaseModel):
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo" : {
                "email" : "test@test.com",
                "password" : "1111"
            }
        }

# In-memory storage 
contacts: List[ContactSchema] = []