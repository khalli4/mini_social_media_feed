"""Routes for post operations"""

from fastapi import APIRouter, Depends, Form, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Post, User
from schemas import LikeCreate

router = APIRouter()


@router.post("/posts/")
def create_post(
    user_id: int = Form(...),
    title: str = Form(...),
    content: str = Form(...),
    image: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    # Make sure the user exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db_post = Post(
        user_id=user_id,
        title=title,
        content=content,
        image_filename=image.filename if image else None
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


@router.get("/posts/")
def list_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()


@router.get("/users/{user_id}/posts")
def list_user_posts(user_id: int, db: Session = Depends(get_db)):
    return db.query(Post).filter(Post.user_id == user_id).all()


@router.post("/posts/{post_id}/like")
def like_post(post_id: int, like: LikeCreate, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        return {"error": "Post not found"}
    post.likes += 1
    db.commit()
    return {"message": f"{like.username} liked post {post_id}"}
