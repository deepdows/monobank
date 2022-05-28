from config import templates
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get('/login', response_class=HTMLResponse)
@router.get('/', response_class=HTMLResponse)
def home_view(request: Request):
    return templates.TemplateResponse("index.html", {'request': request})