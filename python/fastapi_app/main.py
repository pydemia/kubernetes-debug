from typing import Union

import logging
import socket
from fastapi import FastAPI


app = FastAPI()

log = logging.getLogger("fastapi_app")
log.setLevel("DEBUG")

@app.get("/")
def read_root():
    log.debug(f"request to: 'read_root'")
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    resp = {
        "item_id": item_id,
        "q": q,
        "machine": socket.gethostname(),
    }
    log.debug(f"request to: 'read_item'")
    log.debug(f"response is:\n{resp}")
    return resp
