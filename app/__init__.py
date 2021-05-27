from fastapi import FastAPI

from logs import log_init, sys_log
from utils.common_util import write_log
from middleware import middleware_init
from routers import router_init

def conf_init(app):
    from config import configs
    sys_log.info(msg=f'Start application with {configs.ENVIRONMENT} environment')
    if configs.ENVIRONMENT == 'production':
        app.docs_url = None
        app.redoc_url = None
        app.debug = False


async def start_event():
    await write_log(msg='Application is started')


async def shutdown_event():
    await write_log(msg='Application is shutdown')


def create_app():
    app = FastAPI(title="ALGO_DEMO_API",
                  description="算法模块接口说明",
                  version="1.0.0",
                  on_startup=[start_event],
                  on_shutdown=[shutdown_event]
                  )

    log_init()
    conf_init(app)
    router_init(app)
    middleware_init(app)
    return app
