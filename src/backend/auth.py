from datetime import datetime, timedelta
from typing import Optional

import jwt
from fastapi import HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from config import SECRET_KEY

ALGORITHM = "HS256"

security = HTTPBearer()

def create_access_token(data, expire_minutes: Optional[int] = None):
    if expire_minutes:
        expire = datetime.utcnow() + timedelta(expire_minutes)
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    encoded_jwt = jwt.encode({
        'sub': data,
        'exp': expire,
    }, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='Signature has expired')
    except jwt.InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')


def get_current_user(auth: HTTPAuthorizationCredentials = Security(security)):
    return verify_token(auth.credentials)
