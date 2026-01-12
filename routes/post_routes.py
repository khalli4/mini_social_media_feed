"""Routes for post operations"""

from auth_routes import get_current_user
from fastapi import APIRouter, Depends, Form, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Post, User
from schemas import LikeCreate

router = APIRouter(prefix="/posts", tags=["Posts"])

# ---------------- CREATE ---------------- #


@router.post("/")
def create_post(
    title: str = Form(...),
    content: str = Form(...),
    image: UploadFile = File(None),
    current_user: User = Depends(get_current_user),  # 🔑 requires token
    db: Session = Depends(get_db)
):
    db_post = Post(
        user_id=current_user.id,
        title=title,
        content=content,
        image_filename=image.filename if image else None
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

# ---------------- READ ---------------- #


@router.get("/")
def list_posts(db: Session = Depends(get_db)):
    """List all posts"""
    return db.query(Post).all()


@router.get("/{post_id}")
def get_post(post_id: int, db: Session = Depends(get_db)):
    """Get a single post by ID"""
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.get("/user/{username}")
def list_user_posts(username: str, db: Session = Depends(get_db)):
    """List all posts by a specific user"""
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return db.query(Post).filter(Post.user_id == user.id).all()

# ---------------- UPDATE ---------------- #


@router.put("/{post_id}")
def update_post(
    post_id: int,
    title: str,
    content: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update a post by ID (only if owner)"""
    post = db.query(Post).filter(Post.id == post_id,
                                 Post.user_id == current_user.id).first()
    if not post:
        raise HTTPException(
            status_code=404, detail="Post not found or not owned by you")
    post.title = title
    post.content = content
    db.commit()
    return {
        "message": "Post updated successfully",
        "post": {"id": post.id, "title": post.title, "content": post.content}
    }

# ---------------- DELETE ---------------- #


@router.delete("/{post_id}")
def delete_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete a post by ID (only if owner)"""
    post = db.query(Post).filter(Post.id == post_id,
                                 Post.user_id == current_user.id).first()
    if not post:
        raise HTTPException(
            status_code=404, detail="Post not found or not owned by you")
    db.delete(post)
    db.commit()
    return {"message": f"Post {post_id} deleted successfully"}

# ---------------- LIKE ---------------- #


@router.post("/{post_id}/like")
def like_post(post_id: int, like: LikeCreate, db: Session = Depends(get_db)):
    """Like a post"""
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    post.likes += 1
    db.commit()
    return {"message": f"{like.username} liked post {post_id}", "likes": post.likes}
