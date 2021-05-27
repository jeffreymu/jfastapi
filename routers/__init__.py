from routers import demo_view
from api.api_v1.endpoints import testapi
from config import configs


def router_init(app):
    app.include_router(
        demo_view.router,
        prefix=configs.API_V1_STR,
        tags=["Test_Demo"],
        responses={404: {"description": "Not found"}},
    )

    app.include_router(
        testapi.router,
        prefix=configs.API_V1_STR,
        tags=["Test_Demo"],
        responses={404: {"description": "Not found"}},
    )



