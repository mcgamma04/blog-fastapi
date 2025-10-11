from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import models, database
from routes import  post_routes, user_routes
from routes.auth_router import router as auth_router


# Create all tables at startup
models.Base.metadata.create_all(bind=database.engine)

# Initialize FastAPI app
app = FastAPI(title="User Management API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# routes
app.include_router(user_routes.router)
app.include_router(post_routes.router)
app.include_router(auth_router)


# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to User Management API"}
