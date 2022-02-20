from .auth import auth_middleware

MIDDLEWARES = [
    auth_middleware,
]

__all__ = ['MIDDLEWARES']
