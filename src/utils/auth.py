from aiohttp.web_response import json_response


def access_token_required(func):
    def wrapper(request):
        if not request.user:
            return json_response({'message': 'Auth required'}, status=401)
        return func(request)

    return wrapper

