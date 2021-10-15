import uvicorn

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.requests import Request

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def page_home():
    return """
        <h1>
            Hello my name is Ethan
        </h1>
        """


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
