from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .receipts.router import router as r_router
from .auth.router import router as a_router

app: FastAPI = FastAPI()

origins: tuple[str, str] = (
    "http://localhost",
    "http://localhost:3000"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)



@app.head("/",status_code=200)
async def read_root():
    return {"detail": "Connected Successfully!"}


app.include_router(r_router)
app.include_router(a_router)

if __name__ == "__main__":
    import uvicorn
    import socket


    def is_server_running(host: str, port: int) -> bool:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                s.connect((host, port))
                return True
        except (ConnectionRefusedError, socket.timeout):
            return False


    def start_uv_server():
        host: str = "127.0.0.1"
        port: int = 8000
        if not is_server_running(host, port):
            uvicorn.run(app, host=host, port=port)
        else:
            print("Server is already running.")


    start_uv_server()
