from aiohttp import web

from . import views

HTTP_ROUTES = [web.get('/sensors/temperature', views.sensors.get_temperature_data),
               web.post('/login', views.login),
               web.post('/recuperator/change_mode', views.change_recuperator_mode),
               web.get('/sensors/humidity', views.sensors.get_humidity_data),
               web.get('/sensors/heat', views.sensors.get_heat_data),
               web.post('/recuperator/change_schedule/', views.change_recuperator_schedule)]
