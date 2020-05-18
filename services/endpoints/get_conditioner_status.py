import sqlite3


async def get_conditioner_status_data():
    sqlite_connection = sqlite3.connect('SmartHome.db')
    cursor = sqlite_connection.cursor()

    cursor.execute('SELECT name from sqlite_master where type= "table"')

    sqlite_select_query = """SELECT * from CONDITIONER_DATA"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    return records
