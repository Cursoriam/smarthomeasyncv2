from aiohttp import web

from . import views

HTTP_ROUTES = [web.get('/conditioner/status', views.appliances.conditioner.get_conditioner_status)]
