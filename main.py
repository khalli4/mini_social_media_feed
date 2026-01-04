from fastapi import APIRouter
from fastapi import FastAPI
from routes import user_routes, post_routes

app = FastAPI(title="Mini Social Media Feed")

# Include routers
app.include_router(user_routes.router, tags=["Users"])
app.include_router(post_routes.router, tags=["Posts"])
# ...existing code...

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.get("/")
def list_posts():
    return {"posts": []}
# ...existing code...


@app.get("/")
def root():
    return {"message": "Welcome to Mini Social Media Feed API"}
