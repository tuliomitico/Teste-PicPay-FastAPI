import traceback
from typing import List, Optional, Union

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

from src import __version__
from src.database.db import db_session
from src.repositories.user import get_user_by_document
from src.services.transaction import TransactionService
from src.services.user import UserService
from src.schemas.user import UserCreate, User as UserSchema
from src.schemas.transaction import Transaction, TransactionDTO
from src.utils.error import TransactionException

app = FastAPI(version=__version__)

@app.exception_handler(TransactionException)
def exception_handler(request: Request, exc: TransactionException):
    traceback.print_exception(etype=exc.__class__, value=exc, tb=exc.__traceback__)
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message,"statusCode": exc.status_code},
    )

@app.exception_handler(IntegrityError)
def integrity_exception_handler(request: Request, exc: IntegrityError):
    traceback.print_exception(etype=exc.orig, value=exc, tb=exc.__traceback__)
    return JSONResponse(
        status_code=400,
        content={"message": "Usuário já cadastrado","statusCode": 400},
    )

@app.exception_handler(Exception)
def general_exception_handler(request: Request, exc: Exception):
    traceback.print_exception(etype=exc.__class__, value=exc, tb=exc.__traceback__)
    return JSONResponse(
        status_code=500,
        content={"message": str(exc),"statusCode": 500},
    )
@app.on_event("shutdown")
def shutdown(): 
    db_session.remove()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/users/search",response_model=Union[UserSchema,List[UserSchema]])
def get_user_by_document_view(document: Optional[str] = None):
    print(document)
    return get_user_by_document(document)

@app.get("/users/{user_id}",response_model=UserSchema)
def get_user_by_id_view(user_id: int):
    try:
        return UserService().find_user_by_id(user_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail={"message":str(e),"statusCode": 404})

@app.post("/users/",status_code=201)
def create_user_view(user: UserCreate) -> UserSchema:
   return UserService().save_user(user)

@app.get("/users/")
def get_all_users_view():
    return UserService().find_all() 


@app.post("/transactions/",status_code=201)
def create_transaction_view(transaction: TransactionDTO) -> Transaction:
    return TransactionService().create_transaction(transaction)