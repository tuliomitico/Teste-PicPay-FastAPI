import sqlalchemy as sa

from ...database.db import Base, db_session

class User(Base):
    __tablename__ = "users"
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String)
    last_name = sa.Column(sa.String)
    document = sa.Column(sa.String, unique=True)
    email = sa.Column(sa.String, unique=True)
    password = sa.Column(sa.String)
    balance = sa.Column(sa.Float)
    user_type = sa.Column(sa.String)

    def __init__(self,first_name,last_name,document,email,password,balance,user_type,*args,**kwargs) -> None:
        super(User,self).__init__(*args,**kwargs)
        self.first_name = first_name
        self.last_name = last_name
        self.document = document
        self.email = email
        self.password = password
        self.balance = balance
        self.user_type = user_type

    def create(self):
        try:
            db_session.add(self)
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            raise e
        return self
        