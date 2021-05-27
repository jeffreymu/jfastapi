from typing import Optional, Dict, List
from pydantic import BaseModel

class DemoBaseResponse(BaseModel):
    """
    返回数据的基础结构
    """
    status_code: int
    msg: str

class DemoResponse(DemoBaseResponse):
    data: Optional[List] = None
