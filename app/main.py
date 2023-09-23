from fastapi import FastAPI
import uvicorn

from .routers import users, products

app = FastAPI()

app.include_router(users.router)
app.include_router(products.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()