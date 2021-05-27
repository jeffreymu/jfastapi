from datetime import datetime


class CommonQueryParams(object):
    def __init__(self, q: str = None, skip: int = 0, limit: int = 10):
        self.q = q
        self.skip = skip
        self.limit = limit


async def write_log(api=None, msg=None, user='root'):
    with open("log.log", mode="a", encoding='utf-8') as log:
        now = datetime.now()
        log.write(f"Time：{now}    API Invoke：{api}    user：{user}    message：{msg}\n")
