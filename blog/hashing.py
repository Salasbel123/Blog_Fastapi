from fastapi import FastAPI
from passlib.context import CryptContext

schemes = {
    "bcrypt": "bcrypt",
}

pwd_cxt=CryptContext(schemes["bcrypt"], deprecated="auto")

# class Hash():
#     def bcrypt(password:str):
#         return pwd_cxt.hash(password)

class Hash:
    @staticmethod
    def bcrypt(password: str) -> str:
        return pwd_cxt.hash(password)
    
    def verify(hash_password , plain_password):
        return pwd_cxt.verify(plain_password,hash_password)