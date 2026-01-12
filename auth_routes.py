from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, APIRouter, Form
from sqlalchemy.orm import Session
from database import get_db
from models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


SECRET_KEY = "supersecretkey"   # change this in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# 🔑 Security scheme for Swagger
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# 👇 Router definition
router = APIRouter(prefix="/auth", tags=["Auth"])

# ---------------- AUTH ENDPOINTS ---------------- #


@router.post("/login")
def oauth_login(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}


@router.get("/me")
def read_current_user(current_user: User = Depends(lambda: get_current_user())):
    return {"username": current_user.username}


@router.get("/verify")
def verify_token(current_user: User = Depends(lambda: get_current_user())):
    return {"status": "valid", "user": current_user.username}


@router.post("/logout")
def logout():
    # Note: JWT logout is client-side (discard token)
    return {"message": "Successfully logged out. Please discard your token."}

# ---------------- HELPER ---------------- #


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user
