import pickle

from fastapi import APIRouter
from utils.constants import HTTP
from model.schema_demo import DemoResponse

router = APIRouter()


@router.get("/demo", response_model=DemoResponse)
async def demo():
    print("print demo message")
    return {'status_code': HTTP.HTTP_200_OK, "msg": "OK", 'data': ["test data"]}