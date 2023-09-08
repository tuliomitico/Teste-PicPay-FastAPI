from src.database.db import engine, db_session
from src.models.user.user import User
from src.schemas.user import User as UserSchema

def get_user_by_document(document: str):
    sql_statement = User.query.statement.compile(engine, compile_kwargs={"literal_binds": True}).string
    print(sql_statement)
    if document:
        return User.query.filter(User.document == document).first()
    print( User.query.order_by(User.id.desc()).statement.compile(engine, compile_kwargs={"literal_binds": True}).string)
    return User.query.order_by(User.id.desc()).all()

def get_user_by_id(id: int):
    sql_statement = User.query.filter(User.id == id).statement.compile(engine, compile_kwargs={"literal_binds": True}).string
    print(sql_statement)
    return User.query.filter(User.id == id).one_or_none()

def create_user(user: UserSchema) -> User:
    db_user = User(**user.model_dump())
    try:
        db_session.add(db_user)
        db_session.commit()
        db_session.refresh(db_user)
    except:
        db_session.rollback()
        raise
    return db_user