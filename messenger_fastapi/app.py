import time
 
from fastapi import FastAPI, Request
from api.User import router as user_router

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    print("shomare1")
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


app.include_router(user_router, prefix="/api")


# TODO: model? baraye messenger
# TODO: authentication
# TODO: Dependency
# TODO: websocket
