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

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def page_home(request: Request):
    db = shelve.open(f"{BASEDIR}/database/db")
    notes = dict(db)
    db.close()
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "View Notes", "notes": notes}
    )


@app.get("/create", response_class=HTMLResponse)
def page_create_notes(request: Request):
    return templates.TemplateResponse(
        "create_notes.html", {"request": request, "title": "Create Notes"}
    )


@app.post("/create")
def create_notes(subject: str = Form(...), content: str = Form(...)):
    with shelve.open(f"{BASEDIR}/database/db") as db:
        uuid = str(uuid4())[:8]
        db[uuid] = {
            "id": uuid,
            "subject": subject,
            "content": content,
            "date_created": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        }
        db.close()
    return RedirectResponse(url="/create", status_code=302)
