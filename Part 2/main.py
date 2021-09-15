from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

import os

BASEDIR = os.getcwd()

app = FastAPI()
templates = Jinja2Templates(directory=f"{BASEDIR}/templates")

@app.get("/about", response_class=HTMLResponse)
def page_about(request: Request):
    return templates.TemplateResponse(
        "about.html", {"request": request, "title": "About Me"}
    )
