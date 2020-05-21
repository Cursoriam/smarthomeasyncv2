from aiohttp import web

from .http.routes import HTTP_ROUTES


def setup_routes(app: web.Application) -> None:
    app.add_routes(HTTP_ROUTES)
