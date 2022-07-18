import time
 
from fastapi import Depends, FastAPI, Form, Request, HTTPException
from api.User import router as user_router
from api.chat import router as chat_router

async def verify_ip(request: Request):
    if request.client.host == "iran_ip":
        raise HTTPException(status_code=403, detail="Forbidon")
    return request

app = FastAPI(dependencies=[Depends(verify_ip)])


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    print("shomare1")
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}

    
app.include_router(user_router, prefix="/api")
app.include_router(chat_router)


# TODO: model? baraye messenger
# TODO: authentication
# TODO: Dependency
# TODO: websocket
