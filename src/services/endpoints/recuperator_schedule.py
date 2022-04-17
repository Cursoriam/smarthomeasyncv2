# TODO: Refactor
from aiohttp import web
from src.sqlite import recuperator_schedule_manager
from src.sqlite import recuperator_data_db_manager


async def add_or_update_recuperator_schedule(request: web.Request):
    request_data = await request.json()
    for data in request_data['data']:
        if data['schedule_status'] == "delete":
            for schedule in data['schedules']:
                schedules_to_delete = [schedule['id']]
                recuperator_data_db_manager.execute_single_command(recuperator_schedule_manager.create_delete_command(),
                                                                   schedules_to_delete)
        elif data['schedule_status'] == "add":
            for schedule in data['schedules']:
                schedule_to_add = [schedule['start_time'], schedule['end_time'], schedule['temperature']]
                recuperator_data_db_manager.execute_single_command(recuperator_schedule_manager.create_insert_command(),
                                                                   schedule_to_add)
        elif data['schedule_status'] == "update":
            for schedule in data['schedules']:
                schedule_to_update = [schedule['start_time'], schedule['end_time'], schedule['temperature'], schedule['id']]
                recuperator_data_db_manager.execute_single_command(recuperator_schedule_manager.create_update_command(),
                                                                   schedule_to_update)
