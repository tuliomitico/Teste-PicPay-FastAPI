from pydantic import BaseModel

class NotificationDTO(BaseModel):
    email: str
    message: str
