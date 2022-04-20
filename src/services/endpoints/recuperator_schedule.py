# TODO: Refactor
import json

from aiohttp import web
from src.sqlite import recuperator_schedule_manager
from src.sqlite import recuperator_data_db_manager


async def add_or_update_recuperator_schedule(request: web.Request):
    request_data = await request.json()
    if request_data['schedule_status'] == "delete":
        schedules_to_delete = [request_data['id']]
        recuperator_data_db_manager.execute_single_command(recuperator_schedule_manager.create_delete_command(),
                                                           schedules_to_delete)
    elif request_data['schedule_status'] == "add":
        schedule_to_add = [request_data['start_time'], request_data['end_time'], request_data['temperature']]
        recuperator_data_db_manager.execute_single_command(recuperator_schedule_manager.create_insert_command(),
                                                           schedule_to_add)


async def get_recuperator_schedule_from_db(request: web.Request):
    records = []
    try:
        records = recuperator_data_db_manager.execute_single_command(recuperator_schedule_manager.
                                                                     create_extract_all_command())
    except Exception as err:
        print(err)
    data = [{"id": data[0], "start_time": data[1], "end_time": data[2],
             "temperature": data[3]} for data in records.fetchall()]
    return data
