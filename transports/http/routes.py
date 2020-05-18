from aiohttp import web
from . import views


HTTP_ROUTES = [
    web.get('/conditioner/status', views.conditioner.get_conditioner_status_data)
]
