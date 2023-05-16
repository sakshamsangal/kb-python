import json
import time

import requests
from model.erp import ERP
from fastapi import APIRouter, HTTPException

util = APIRouter()


@util.post('/create-invoice', status_code=201)
def get_dir(item: ERP):
    raise HTTPException(status_code=404, detail="Item not found")
    return item


