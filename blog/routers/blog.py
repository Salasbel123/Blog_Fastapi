from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas,database,models,oauth2
from sqlalchemy.orm import Session

router= APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

get_db=database.get_db
@router.get('/' ,response_model=List[schemas.ShowBlog])
def all(db:Session=Depends(get_db),
current_user:schemas.User=Depends(oauth2.get_current_user)):
        blogs= db.query(models.Blog).all()
        return blogs

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request :schemas.Blog,db:Session=Depends(get_db),
current_user:schemas.User=Depends(oauth2.get_current_user)

):
    new_blog = models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog 

@router.get('/{id}' , status_code=200, 
response_model=schemas.ShowBlog)
def show(id, db:Session =Depends(get_db),
current_user:schemas.User=Depends(oauth2.get_current_user)):
    blog= db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'BLog with this id {id} is not availbale')
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {'detail':f'BLog with this id {id} is not availbale'}
    return blog


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destory(id,db:Session=Depends(get_db),
current_user:schemas.User=Depends(oauth2.get_current_user)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id not found")
    blog.delete(synchronize_session=False)
    
    db.commit()
    return 'Done'


@router.put('/{id}' ,status_code=status.HTTP_202_ACCEPTED)
def update(id,request :schemas.Blog,db:Session=Depends(get_db),
current_user:schemas.User=Depends(oauth2.get_current_user)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND
        ,detail=f"Blog with id {id} not found")
    # blog.update(request)
    blog.update({
        "title": request.title,
        "body": request.body
    })
    db.commit()
    return 'Done'