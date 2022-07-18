from datetime import timedelta
from typing import List, Union

from jose import jwt, JWTError

from fastapi import APIRouter, status, Body, Cookie, Depends, HTTPException, Query, Response
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from config.db import users_collection
from config.security import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY
from crud.User import authenticate_user, retrieve_users, delete_user, update_user , add_user, retrieve_user
from models.User import Token, User, UserInDB, UserOut, UserUpdate
from utils import create_access_token, response_ok_pattern, response_error_pattern


router = APIRouter(prefix="/users", tags=["users"])
oath2_scheme = OAuth2PasswordBearer(tokenUrl="/api/users/token")

async def get_user(username):
    user = await users_collection.find_one({"username": username})
    return user

async def get_current_user(token: str = Depends(oath2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await get_user(username)
    if user is None:
        raise credentials_exception
    return user


def filter_users(q: Union[str, None] = None, age: int = Query(default=18, gt=0), 
                last_query: Union[str, None] = Cookie(default=None)):
    return {"username": q, "age": age, "last_query": last_query}


@router.get("/", response_model=  List[UserOut], response_model_exclude_unset=True)
async def user_list(response: Response, filtering: dict = Depends(filter_users), 
                    token: str = Depends(oath2_scheme)):
    response.set_cookie(key="last_query", value=filtering.get("username"))
    users = []
    if filtering.get("username"):
        async for user in users_collection.find({"$text": {"$search": filtering.get("username")}}):
            users.append(user)
    else:
        async for user in users_collection.find():
            users.append(user)
    return users

# @router.get("/", response_model=  List[UserOut])
# async def user_list():
#     users = await retrieve_users()
#     return response_ok_pattern(users)

@router.get("/{id}")
async def user_detail(id: str):
    try:
        user = await retrieve_user(id)
        return response_ok_pattern(user)
    except Exception as e:
        return response_error_pattern(e)

@router.post("/")
async def user_create(user: UserInDB = Body()):
    new_user = await add_user(jsonable_encoder(user))
    return response_ok_pattern(new_user)

@router.patch("/update")
async def user_update(data: UserUpdate = Body(), user: User = Depends(get_current_user)):
    try:
        data = {k: v for k, v in data.dict().items() if v is not None}
        user = await update_user(user, data)
        return response_ok_pattern("update shod")
    except Exception as e:
        return response_error_pattern(e)

@router.delete("/{id}")
async def user_delete(id: str):
    result = await delete_user(id)
    if result:
        return response_ok_pattern("delete shod")
    else:
        return response_error_pattern("user not found")

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}