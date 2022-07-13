from fastapi import APIRouter, Body, Query
from fastapi.encoders import jsonable_encoder
from crud.User import retrieve_users, delete_user, update_user , add_user, retrieve_user
from models.User import User
from utils import response_ok_pattern, response_error_pattern

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def user_list():
    users = await retrieve_users()
    return response_ok_pattern(users)

@router.get("/{id}")
async def user_detail(id: str):
    try:
        user = await retrieve_user(id)
        return response_ok_pattern(user)
    except Exception as e:
        return response_error_pattern(e)

@router.post("/")
async def user_create(user: User = Body()):
    new_user = await add_user(jsonable_encoder(user))
    return response_ok_pattern(new_user)

@router.put("/{id}")
async def user_update(id: str, data: User = Body()):
    try:
        data = {k: v for k, v in data.dict().items() if v is not None}
        user = await update_user(id, data)
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

