import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.openapi.utils import get_openapi

app = FastAPI()


class Answer(BaseModel):
    question_id: int
    alternative_id: int


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="2.5.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.get("/")
def root():
    return {"message": "Fast API in Python"}




if __name__ == "__main__":
    # uvicorn main:app --reload --port 5000
    uvicorn.run("main:app", host="127.0.0.1", port=8080, log_level="info", reload=True)
