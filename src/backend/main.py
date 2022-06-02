from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

import router as router_api

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="dist")

app.include_router(router_api.router, prefix="/api")

@app.get("/{path_name:path}", response_class=HTMLResponse)
async def home_view(request: Request):
    return templates.TemplateResponse("index.html", {'request': request})

app.mount("/", StaticFiles(directory="dist"), name="static")
