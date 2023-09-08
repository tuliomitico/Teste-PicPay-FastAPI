from typing import NoReturn
import http
import requests

from ..models.user.user import User
from ..schemas.notification import NotificationDTO

class NotificationService:
    def send_notification(self, user: User, message: str) -> None:
        email: str = user.email
        notification_request =  NotificationDTO(email=email,message=message)

        notification_response = requests.post("http://o4d9z.mocklab.io/notify",data={**notification_request.model_dump()})

        if not notification_response == http.HTTPStatus.OK:
            raise Exception("Serviço de notificação indisponível")
        return