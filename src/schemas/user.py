from pydantic import BaseModel

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    document: str
    email: str
    password: str
    balance: float
    user_type: str

    class ConfigDict:
        from_attributes = True

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    document: str
    email: str
    password: str
    balance: float
    user_type: str

    class ConfigDict:
        from_attributes = True