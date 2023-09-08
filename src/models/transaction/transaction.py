import sqlalchemy as sa
from sqlalchemy.orm import relationship 

from ...database.db import Base, db_session
from ..user.user import User

class Transaction(Base):
    __tablename__ = "transactions"
    id = sa.Column(sa.Integer, primary_key=True)
    amount = sa.Column(sa.DECIMAL)
    sender_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    sender = relationship('User',foreign_keys=[sender_id])
    receiver_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    receiver = relationship('User',foreign_keys=[receiver_id])
    timestamp = sa.Column(sa.DateTime,server_default = sa.func.now())

    def __init__(self,amount,sender,receiver,*args,**kwargs) -> None:
        super(Transaction,self).__init__(*args,**kwargs)
        self.amount = amount
        self.sender = sender
        self.receiver = receiver
        self.sender_id = sender.id
        self.receiver_id = receiver.id
    def create(self):
        try:
            db_session.add(self)
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            raise e
        return self