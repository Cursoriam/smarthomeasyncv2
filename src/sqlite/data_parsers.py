import json


def temperature_data_parser(json_data: str):
    data = json.loads(json_data)
    return data


def humidity_data_parser(json_data: str):
    data = json.loads(json_data)
    return data


def co2_data_parser(json_data: str):
    data = json.loads(json_data)
    return data
