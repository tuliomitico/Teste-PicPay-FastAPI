from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

engine = create_engine('sqlite:///./test.db',connect_args={'check_same_thread':False})

db_session = scoped_session(sessionmaker(engine,autoflush=False,autocommit=False))

Base = declarative_base()

Base.query = db_session.query_property()