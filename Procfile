web: gunicorn --pythonpath src/main:init --timeout 90 --worker-class aiohttp.GunicornWebWorker & python dummy/__init__.py & wait -n
