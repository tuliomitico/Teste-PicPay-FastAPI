import requests
import http

from ..models.transaction.transaction import Transaction
from ..models.user.user import User
from ..schemas.transaction import TransactionDTO
from ..services.user import UserService
from ..services.notification import NotificationService
from ..utils.error import TransactionException

class TransactionService():
    __user_service: UserService
    __notification_service: NotificationService
    def __init__(self) -> None:
        self.__user_service = UserService()
        self.__notification_service = NotificationService()
    def create_transaction(self, transaction: TransactionDTO) -> Transaction:
        sender: User = self.__user_service.find_user_by_id(transaction.sender_id)
        receiver: User = self.__user_service.find_user_by_id(transaction.receiver_id)

        self.__user_service.validate_transaction(sender, transaction.value)

        is_authorized = self.authorize_transaction(sender,transaction.value)
        if not is_authorized:
            raise TransactionException("Transação não autorizada",status_code=400)
        
        new_transaction = Transaction(transaction.value, sender, receiver).create()
        
        sender.balance -= transaction.value
        receiver.balance += transaction.value

        sender.create()
        receiver.create()

        # self.__notification_service.send_notification(sender, "Transação realizada com sucesso.")
        # self.__notification_service.send_notification(receiver, "Transação recebida com sucesso.")
        print("Notificação enviada para o usuário {0} e {1}".format(sender.first_name,receiver.first_name))
        return new_transaction

    def authorize_transaction(self,sender: User, amount: float) -> bool:
        authorization_response = requests.get('https://run.mocky.io/v3/8fafdd68-a090-496f-8c9a-3442cf30dae6')

        if authorization_response.status_code == http.HTTPStatus.OK:  
            message: str = authorization_response.json()['message']
            return "Autorizado".lower() == message.lower()
        return False
