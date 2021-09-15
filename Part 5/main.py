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

@app.get("/", response_class=HTMLResponse)
def page_home(request: Request):
    db = shelve.open(DBDIR)
    notes = dict(db)
    db.close()
    return templates.TemplateResponse(
        "view_notes.html", {"request": request, "title": "View Notes", "notes": notes}
    )

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

@app.post("/delete")
def notes_delete(uuid: str = Form(...)):
    print(uuid)
    db = shelve.open(DBDIR)
    del db[uuid]
    db.close()
    return RedirectResponse(url="/", status_code=302)

@app.get("/update/{uuid}")
def page_notes_update(request: Request, uuid):
    db = shelve.open(DBDIR)
    target = db[uuid]
    db.close()
    print(target)
    return templates.TemplateResponse(
        "update_notes.html", {"request": request, "data": target}
    )


@app.post("/update")
def notes_update(
        uuid: str = Form(...), subject: str = Form(...), content: str = Form(...)
):
    db = shelve.open(DBDIR)
    data = db[uuid]

    data["subject"] = subject
    data["content"] = content
    data["date_updated"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    db[uuid] = data
    db.close()
    return RedirectResponse(url="/", status_code=302)
