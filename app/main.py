from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import models, database
from routes import post_routes, user_routes


# Create all tables at startup
models.Base.metadata.create_all(bind=database.engine)

# Initialize FastAPI app
app = FastAPI(title="User Management API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict later, e.g., ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# routes
app.include_router(user_routes.router)
app.include_router(post_routes.router)


# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to User Management API"}
