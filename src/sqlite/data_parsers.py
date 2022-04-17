import json


def temperature_data_parser(json_data: str):
    data = json.loads(json_data)
    return data


def humidity_data_parser(json_data: str):
    data = json.loads(json_data)
    return data


def heat_data_parser(json_data: str):
    data = json.loads(json_data)
    return data


def recuperator_schedule_parser(json_data: str):
    data = json.loads(json_data)
    return data
