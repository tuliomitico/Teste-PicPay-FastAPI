import uvicorn 
from src.models.user.user import User
from src.models.transaction.transaction import Transaction
from src.database.db import Base, engine

if __name__ == "__main__":
    # Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)
    uvicorn.run("server:app", host="0.0.0.0", port=5000, reload=True,app_dir='src')