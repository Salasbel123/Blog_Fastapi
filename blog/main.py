# from typing import List
# from fastapi import FastAPI, Depends,status,Response,HTTPException
# from . import schemas,models,hashing
# from .hashing import Hash
# from .database import engine,get_db
# from sqlalchemy.orm import Session
from . import models
from fastapi import FastAPI
from .database import engine
from .routers import blog,user,authentication



models.Base.metadata.create_all(engine)
  

# def get_db():
#     db=SessionLoacl()
#     try:
#         yield db
#     finally:
#         db.close()

app= FastAPI()
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)



# @app.post('/blog',status_code=status.HTTP_201_CREATED, tags=['Blogs'])
# def create(request :schemas.Blog,db:Session=Depends(get_db)):
#     new_blog = models.Blog(title=request.title,body=request.body,user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog 
#/////////////////////
# @app.get('/blog' , tags=['Blogs'])
# def all(db:Session=Depends(get_db)):
#         blogs= db.query(models.Blog).all()
#         return blogs
#/////////
# @app.get('/blog/{id}' , status_code=200, 
# response_model=schemas.ShowBlog, tags=['Blogs'])
# def show(id, response:Response,db:Session =Depends(get_db)):
#     blog= db.query(models.Blog).filter(models.Blog.id==id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#         detail=f'BLog with this id {id} is not availbale')
#         # response.status_code=status.HTTP_404_NOT_FOUND
#         # return {'detail':f'BLog with this id {id} is not availbale'}
#     return blog


# @app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT, tags=['Blogs'])
# def destory(id,db:Session=Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id==id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id not found")
#     blog.delete(synchronize_session=False)
    
#     db.commit()
#     return 'Done'


# @app.put('/blog/{id}' ,status_code=status.HTTP_202_ACCEPTED, tags=['Blogs'])
# def update(id,request :schemas.Blog,db:Session=Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id==id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND
#         ,detail=f"Blog with id {id} not found")
#     # blog.update(request)
#     blog.update({
#         "title": request.title,
#         "body": request.body
#     })
#     db.commit()
#     return 'Done'




# @app.post('/user', response_model=schemas.ShowUser, tags=['Users'])
# def create_user(request:schemas.User,db:Session=Depends(get_db)):
#     # hashedPassword=pwd_cxt.hash(request.password)
#     new_user = models.User(name=request.name,email=request.email
#     ,password=Hash.bcrypt(request.password))
#     # password=request.password)
#     # password=Hash.bcrypt(request.password)
#     # new_user=models.User(request)
#     db.add(new_user)
#     db.commit()
#     # db.refresh()
#     db.refresh(new_user)
 
#     return request

# @app.get('/user/{id}', response_model=schemas.ShowUser, tags=['Users'])
# def get_user(id:int,db:Session=Depends(get_db)):
#     user= db.query(models.User).filter(models.User.id==id).first()
#     if not user:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND
#        , detail=f"User with this id {id} not exsit")

#     return user
