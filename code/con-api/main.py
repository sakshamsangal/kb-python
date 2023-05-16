import uvicorn
from fastapi import FastAPI

from controller import controller_create_invoice

app = FastAPI()

app.include_router(controller_create_invoice.util)

if __name__ == "__main__":
    # uvicorn main:app --reload --port 5000
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload=True)
