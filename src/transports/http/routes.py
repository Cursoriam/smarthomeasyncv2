from aiohttp import web

from . import views

HTTP_ROUTES = [web.get('/sensors/temperature', views.sensors.get_temperature_data)]
