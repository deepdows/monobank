from decimal import Decimal

import requests
from cachetools import TTLCache, cached
from fastapi import APIRouter, Depends, HTTPException, status

from auth import create_access_token, get_current_user
from config import API_TOKEN, user
from schemas import AuthSchema

router = APIRouter()
cache = TTLCache(maxsize=1000, ttl=65)
print(API_TOKEN)
@router.post('/login/')
async def login(auth_details: AuthSchema):
    auth_details.username = auth_details.username.strip()
    if (auth_details.password != user.get('password')
            or auth_details.username != user.get('username')):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid username or password"
        )
    token = create_access_token(user['username'], expire_minutes=30)
    return {'token': token}

@cached(cache)
def request():
    return requests.get(
        url='https://api.monobank.ua/personal/client-info',
        headers={'X-Token': API_TOKEN}
    ).json()

@router.get("/cards/")
async def balance(current_user=Depends(get_current_user)):
    response = request()
    cards = []
    accounts = response['accounts']
    for i in range(len(accounts)):
        if accounts[i]['balance'] and accounts[i]["currencyCode"] == 980:
            cards.append({
                'balance': '{:,}'.format(Decimal(accounts[i]['balance']) / Decimal(100)),
                'card': accounts[i]['maskedPan'][0],
            })
    return cards
