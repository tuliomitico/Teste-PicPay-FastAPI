from typing import NoReturn

from ..models.user.user import User
from ..schemas.user import UserCreate
from ..utils.error import TransactionException

class UserService():
    def validate_transaction(self,sender: User, amount: float) -> Exception:
        if (sender.user_type == "Merchant"):
            raise TransactionException("Usuário do tipo Lojista não está autorizado a realizar transações.",400)
        if (sender.balance < amount):
            raise TransactionException("Saldo insuficiente",status_code=400)
        
    def find_user_by_id(self, user_id: int) -> User:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return user
        raise Exception("Usuário não encontrado.")
    
    def save_user(self, user: UserCreate) -> NoReturn:
        new_user = User(**user.model_dump()).create()
        return new_user
    
    def find_all(self):
        users = User.query.all()
        return users