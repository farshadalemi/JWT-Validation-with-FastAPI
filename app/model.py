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

# In-memory storage 
contacts: List[ContactSchema] = []