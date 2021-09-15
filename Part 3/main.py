from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

import os
import shelve
from uuid import uuid4
from datetime import datetime

BASEDIR = os.getcwd()
DBDIR = f"{BASEDIR}/database/db"

app = FastAPI()
templates = Jinja2Templates(directory=f"{BASEDIR}/templates")

@app.get("/about", response_class=HTMLResponse)
def page_about(request: Request):
    return templates.TemplateResponse(
        "about.html", {"request": request, "title": "About Me"}
    )

@app.get("/create", response_class=HTMLResponse)
def page_notes_create(request: Request):
    return templates.TemplateResponse(
        "create_notes.html", {"request": request, "title": "Create Notes"}
    )

@app.post("/create")
def notes_create(subject: str = Form(...), content: str = Form(...)):
    db = shelve.open(DBDIR)
    uuid = str(uuid4())[:8]
    db[uuid] = {
        "id": uuid,
        "subject": subject,
        "content": content,
        "date_created": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "date_updated": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    }
    db.close()
    return RedirectResponse(url="/create", status_code=302)
