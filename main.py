from fastapi import FastAPI
from routes import user_routes, post_routes
from auth_routes import router as auth_router

app = FastAPI(title="Mini Social Media Feed")

app.include_router(user_routes.router)
app.include_router(post_routes.router)
app.include_router(auth_router)   # 👈 include the auth router


@app.get("/")
def root():
    return {"message": "Welcome to Mini Social Media Feed API"}
