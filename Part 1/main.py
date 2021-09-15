from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.requests import Request

app = FastAPI()

@app.get("/about", response_class=HTMLResponse)
def page_about(request: Request):
    return """
        <h1>
            Hello my name is Ethan
        </h1>
        """

