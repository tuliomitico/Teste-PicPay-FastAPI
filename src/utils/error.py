class TransactionException(Exception):
    def __init__(self,message:str,status_code: int) -> None:
        self.status_code = status_code
        self.message = message