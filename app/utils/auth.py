# # from datetime import datetime, timedelta
# # from jose import JWTError, jwt
# # from fastapi import Depends, HTTPException, status
# # from fastapi.security import OAuth2PasswordBearer
# # from sqlalchemy.orm import Session
# # from app import schemas, models, database
# # from app.utils import verify_password
# # import os
# # from dotenv import load_dotenv

# # load_dotenv()

# # SECRET_KEY = os.getenv("JWT_SECRET_KEY")
# # ALGORITHM = os.getenv("JWT_ALGORITHM")
# # ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

# # oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# # def create_access_token(data: dict):
# #     """Generate JWT token for a user."""
# #     to_encode = data.copy()
# #     expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
# #     to_encode.update({"exp": expire})
# #     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# # def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.SessionLocal)):
# #     """Get user from token (protect endpoints)."""
# #     credentials_exception = HTTPException(
# #         status_code=status.HTTP_401_UNAUTHORIZED,
# #         detail="Could not validate credentials",
# #         headers={"WWW-Authenticate": "Bearer"},
# #     )

# #     try:
# #         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
# #         user_id: int = payload.get("user_id")
# #         if user_id is None:
# #             raise credentials_exception
# #     except JWTError:
# #         raise credentials_exception

# #     user = db.query(models.User).filter(models.User.id == user_id).first()
# #     if user is None:
# #         raise credentials_exception
# #     return user


# from datetime import datetime, timedelta
# from jose import JWTError, jwt
# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from sqlalchemy.orm import Session
# from app import models, database
# import os
# from dotenv import load_dotenv

# load_dotenv()

# SECRET_KEY = os.getenv("JWT_SECRET_KEY")
# ALGORITHM = os.getenv("JWT_ALGORITHM")
# ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# def create_access_token(data: dict):
#     """Generate JWT token for a user."""
#     to_encode = data.copy()
#     expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# def get_current_user(
#     token: str = Depends(oauth2_scheme), db: Session = Depends(database.SessionLocal)
# ):
#     """Get user from token (protect endpoints)."""
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )

#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         user_id: int = payload.get("user_id")
#         if user_id is None:
#             raise credentials_exception
#     except JWTError:
#         raise credentials_exception

#     user = db.query(models.User).filter(models.User.id == user_id).first()
#     if user is None:
#         raise credentials_exception
#     return user


# from datetime import datetime, timedelta
# from jose import JWTError, jwt
# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from sqlalchemy.orm import Session
# from app import models, database
# import os
# from dotenv import load_dotenv

# load_dotenv()

# SECRET_KEY = os.getenv("JWT_SECRET_KEY")
# ALGORITHM = os.getenv("JWT_ALGORITHM")
# ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

# # This defines the token endpoint Swagger will use for authentication
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# def create_access_token(data: dict):
#     """Generate a JWT access token."""
#     to_encode = data.copy()
#     expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# def get_current_user(
#     token: str = Depends(oauth2_scheme), db: Session = Depends(database.SessionLocal)
# ):
#     """Retrieve the current user from the JWT token."""
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )

#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         user_id: int = payload.get("user_id")
#         if user_id is None:
#             raise credentials_exception
#     except JWTError:
#         raise credentials_exception

#     user = db.query(models.User).filter(models.User.id == user_id).first()
#     if user is None:
#         raise credentials_exception
#     return user


# app/utils/auth.py
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app import models, database
from app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def create_access_token(data: dict):
    """Generate a JWT access token. SECRET_KEY must be a str (not None)."""
    if not SECRET_KEY or not isinstance(SECRET_KEY, str) or SECRET_KEY.strip() == "":
        raise RuntimeError("Missing or invalid SECRET_KEY. Check app/config.py and your .env file.")

    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    # jose will accept either str or bytes; pass str here
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.SessionLocal)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise credentials_exception
    return user
