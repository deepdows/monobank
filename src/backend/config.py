from fastapi.templating import Jinja2Templates
import os

if os.environ.get('ENV', None):
    from dotenv import load_dotenv
    load_dotenv()

API_TOKEN = os.environ.get('API_TOKEN')
SECRET_KEY = os.environ.get('SECRET_KEY')

user = {
    'username': os.environ.get('ADMIN_USERNAME'),
    'password': os.environ.get('ADMIN_PASSWORD')
}

templates = Jinja2Templates(directory="dist")
