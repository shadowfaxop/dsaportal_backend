from datetime import datetime,date
import os
import base64
import pymysql
from pymysql import converters
import pandas as pd
import mysql.connector as db
 
 
HOST="widget-dev.c8mrfyuk9eoc.ap-south-1.rds.amazonaws.com"
USERNAME="posdev"
PASSWORD="FAT4NMH%40ZWVTkt8"
DATABASE_NAME="posdev"
 
def connect_B2B_db():
    converions = converters.conversions
    converions[pymysql.FIELD_TYPE.DATE] = lambda x: str(x)
    converions[pymysql.FIELD_TYPE.DATETIME] = lambda x: str(x)
    converions[pymysql.FIELD_TYPE.TIMESTAMP] = lambda x: str(datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S"))
    converions[pymysql.FIELD_TYPE.LONGLONG] = lambda x: str(x)
    return pymysql.connect(HOST, USERNAME, PASSWORD, DATABASE_NAME,conv=converions)
 
def execute_query(query, dBtype):
    try:
        if dBtype == "B2B":
            conn=connect_B2B_db()
                       
        cursor=conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query)
        return True, cursor
    except Exception as e:
        print(e)
        return False, None
    finally:
        conn.close()
 
main_query = f'''
select now();
'''
print("Executing MAIN QUERY ... ",datetime.now().strftime("%H:%M:%S"))
success,result_main=execute_query(main_query, "POS")
excel_main = pd.DataFrame(result_main)
print(excel_main)