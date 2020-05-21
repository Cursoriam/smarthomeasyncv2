from aiohttp import web

HTTP_ROUTES = [
    web.get('/conditioner/status', src.transports.http.views.appliances.conditioner.get_conditioner_status)
]
