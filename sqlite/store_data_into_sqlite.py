import json
import sqlite3

# SQLite DB Name
DB_Name = 'SmartHome.db'


# ===============================================================
# Database Manager Class

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect(DB_Name)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cur = self.conn.cursor()

    def add_del_update_db_record(self, sql_query, args=()):
        self.cur.execute(sql_query, args)
        self.conn.commit()
        return

    def __del__(self):
        self.cur.close()
        self.conn.close()


# ===============================================================
# Functions to push Sensor Data into Database

# Function to save Temperature to DB Table
def conditioner_status_data_handler(jsonData):
    # Parse Data
    json_Dict = json.loads(jsonData)
    conditionerID = json_Dict['ConditionerID']
    date_and_time = json_Dict['Date']
    status = json_Dict['Status']

    # Push into DB Table
    dbObj = DatabaseManager()
    dbObj.add_del_update_db_record(
        "insert into CONDITIONER_DATA (ConditionerID, Date_n_Time, Status) values (?,?,?)",
        [conditionerID, date_and_time, status])
    del dbObj
    print("Inserted Temperature Data into Database.")


# ===============================================================
# Master Function to Select DB Funtion based on MQTT Topic

def conditioner_status_handler(Topic, jsonData):
    if Topic == "Home/Conditioner/Status":
        conditioner_status_data_handler(jsonData)
