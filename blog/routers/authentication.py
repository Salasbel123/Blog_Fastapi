from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas,database,models,token
from sqlalchemy.orm import Session
from ..hashing import Hash
router= APIRouter(
    tags=['Authentication']
)
@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends()
, db:Session= Depends(database.get_db)):
    user= db.query(models.User).filter(models.User.email== request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail="Invalid Credentials")
    if not Hash.verify(user.password,request.password):
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail="Incorrect password")
    # return user
      
   
    access_token = token.create_access_token(data={"sub": user.email})
    # encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    # return encoded_jwt
    return {"access_token":access_token,"token_type":"bearer"} 