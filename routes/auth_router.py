# #
# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from pydantic import BaseModel, EmailStr
# from app import models, database
# from app.utils import verify_password
# from app.utils.auth import create_access_token

# router = APIRouter(prefix="/auth", tags=["Authentication"])


# # Dependency to get database session
# def get_db():
#     db = database.SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# # Request model for login
# class LoginRequest(BaseModel):
#     email: EmailStr
#     password: str


# # Response model for token
# class TokenResponse(BaseModel):
#     access_token: str
#     token_type: str = "bearer"


# @router.post("/login", response_model=TokenResponse)
# def login(data: LoginRequest, db: Session = Depends(get_db)):
#     """
#     Authenticate a user using email and password, then issue a JWT access token.
#     """
#     user = db.query(models.User).filter(models.User.email == data.email).first()
#     if not user or not verify_password(data.password, user.password):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid credentials",
#         )

#     # Generate JWT token with user ID
#     token = create_access_token({"user_id": user.id})

#     return {"access_token": token, "token_type": "bearer"}


from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import models, database
from app.utils import verify_password
from app.utils.auth import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    """
    OAuth2 Login — Accepts `username` and `password` form fields.
    Returns a JWT access token on successful authentication.
    """
    # Using email as the username field
    user = db.query(models.User).filter(models.User.email == form_data.username).first()

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token({"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
