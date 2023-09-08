from datetime import datetime
from pydantic import BaseModel

from .user import User

class Transaction(BaseModel):
    amount: float
    sender: User
    receiver: User
    timestamp: datetime

    class ConfigDict:
        from_attributes = True

class TransactionDTO(BaseModel):
    value: float
    sender_id: int
    receiver_id: int
