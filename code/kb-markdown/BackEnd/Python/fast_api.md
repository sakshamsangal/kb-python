# fast API

## set up

```txt
fastapi~=0.85.0
pydantic~=1.10.2
uvicorn~=0.18.3
requests~=2.28.2
```

```python
from fastapi import FastAPI
import uvicorn

app = FastAPI()

if __name__ == "__main__":
    # uvicorn main:app --reload --port 5000
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload=True)

```

## pydantic class

```python
from pydantic import BaseModel


class ERP(BaseModel):
    a1: str
    a2: str

class MSFileName(BaseModel):
    fn: str
    sn: str


class DMFileName(BaseModel):
    fn: str
    sn: str


class DMSheet(BaseModel):
    loc: str
    ct: str
    dm: DMFileName
    ms: MSFileName

```

## router

```python
from fastapi import APIRouter

util = APIRouter()


@util.post('/create-invoice', status_code=201)
def get_dir(item: ERP):
    return item
```

## add router to main

app object is initialised previously

```python
from controller import controller_create_invoice

app.include_router(controller_create_invoice.util)
```

## post
```python
@dm.post("/tag-master", status_code=200)
async def tag_master(item: MapXpath):
    res = ms1.tag_master(item.loc, item.ct, item.fn, item.sn)
    return {'status': res}
```