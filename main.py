from __future__ import annotations

from dotenv import load_dotenv
from fastapi import Depends
from fastapi import FastAPI
from fastapi import Form
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from starlette import status
from starlette.responses import RedirectResponse

from database import SessionLocal
from models import History
from utils import get_coordinates

app = FastAPI()

load_dotenv()
templates = Jinja2Templates(directory='templates')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(request=request, name='index.html', context={})


@app.post('/weather', response_class=HTMLResponse)
async def get_weather(
        request: Request,
        city_name: str = Form(min_length=2, max_length=20),
        db: Session = Depends(get_db),
):
    city_name = str(city_name).strip().title()
    client_ip = request.client.host
    db.add(History(city_name=city_name, user_ip=client_ip))
    db.commit()
    try:
        lat, lon = get_coordinates(city_name)
        temp, feels_like, weather = get_weather(lat, lon)
        return templates.TemplateResponse(
            request=request,
            name='weather.html',
            context={
                'city_name': city_name,
                'temp': temp,
                'feels_like': feels_like,
                'weather': weather,
            },
        )
    except Exception:
        return RedirectResponse(url='/', status_code=status.HTTP_303_SEE_OTHER)


@app.get('/history')
async def history(db: Session = Depends(get_db)):
    return db.query(History.city_name, func.count(History.city_name)).group_by(
        History.city_name,
    )
