from typing import Union

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    a = {"item_id": item_id, "q": q}
    return {"item_id": item_id, "q": q}


# For Debugging

from typing import Callable, Dict
import os
import multiprocessing as mpr
from gunicorn.app.base import BaseApplication


# def number_of_workers():
#     return (mpr.cpu_count() * 2) + 1

# def handler_app(environ: Dict, start_response: Callable):
#     response_body = b"Works fine."
#     status = "200 OK"
#     response_headers = [
#         ("Content-Type", "text/plain"),
#     ]

#     start_response(status, response_headers)

#     return [response_body]


# class StandaloneApp(BaseApplication):

#     def __init__(self, app: Callable, options: Dict = None):
#         self.options = options or {}
#         self.application = app
#         super().__init__()

#     def load_config(self):
#         config = {
#             key: value for key, value in self.options.items()
#             if key in self.cfg.settings and value is not None
#         }

#         for key, value in config.items():
#             self.cfg.set(key.lower(), value)

#     def load(self):
#         return self.application


if __name__ == "__main__":
    # import multiprocessing
    # mpr.set_start_method("spawn", True)

    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))

    # options = {
    #     "bind": f"{HOST}:{APP_PORT}",
    #     "workers": number_of_workers(),
    # }
    # StandaloneApp(handler_app, options).run()

    import uvicorn

    uvicorn.run(app, host=HOST, port=PORT)
