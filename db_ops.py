import psycopg2
import datetime
import json
import os
from dotenv import load_dotenv
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_LOGIN_USER = os.getenv("DB_LOGIN_USER")
DB_LOGIN_PASSWORD = os.getenv("DB_LOGIN_PASSWORD")
DB_SSLMODE = os.getenv("DB_SSLMODE")
table_name = 'public."EvaluationInfos"'

def insert(evaluation_result, model_info_id, user_info_id, test_item):

  # # Construct connection string
  conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(DB_HOST, DB_LOGIN_USER, DB_NAME, DB_LOGIN_PASSWORD, DB_SSLMODE)
  conn = psycopg2.connect(conn_string)
  print("Connection established")
  cursor = conn.cursor()

  # Get the current date and time
  formatted_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  print(formatted_datetime)
  get_time = f"'{formatted_datetime}'"

  # JSON to String
  evaluation_result_string = f"'{json.dumps(evaluation_result)}'"
  
  # Insert Record to DB
  insert_query = f"INSERT INTO {table_name} (\"ModelInfoId\", \"UserInfoId\", \"test_item\", \"evaluation_result\", \"createdAt\", \"updatedAt\") VALUES ({model_info_id}, {user_info_id}, {test_item}, {evaluation_result_string}, {get_time}, {get_time})"
  cursor.execute(insert_query)

  # Clean up
  conn.commit()
  cursor.close()
  conn.close()