import uvicorn

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

import os

BASEDIR = os.getcwd()

app = FastAPI()
templates = Jinja2Templates(directory=f"{BASEDIR}/templates")

@app.get("/", response_class=HTMLResponse)
def page_home(request: Request):
    return templates.TemplateResponse(
        "home.html", {"request": request, "title": "About Me"}
    )


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
