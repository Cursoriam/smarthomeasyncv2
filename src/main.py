import os

from aiohttp import web

from src.bootstrap import init_subscriptions
from src.bootstrap import init_db_dqlite
from src.transports import setup_routes


PORT = int(os.environ.get('PORT', '8088'))


async def init() -> web.Application:
    """
    Инициализация главного aiohttp application
    :return: web.Application
    """
    app = web.Application()
    setup_routes(app)
    init_db_dqlite()
    init_subscriptions()
    return app


if __name__ == '__main__':
    web.run_app(init(), port=PORT)
