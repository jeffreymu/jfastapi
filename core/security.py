from datetime import datetime, timedelta
from typing import Dict, Any

from config import settings

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM

def create_access_token(*, data: dict, expires_delta: timedelta = None) -> Dict[str, Any]:

    return {"code": 201, "msg": "登录成功",
            "data": {"token": "afed234-2341dea-ffea", "username": "jeffrey", "email": "jeffrey@msn.com"}}
