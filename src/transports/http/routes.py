from aiohttp import web

from . import views

HTTP_ROUTES = [web.get('/sensors/temperature', views.sensors.get_temperature_data),
               web.post('/login', views.login),
               web.post('/recuperator/change_mode', views.change_recuperator_mode), ]
