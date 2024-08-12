import mysql.connector
import os
from dotenv import load_dotenv


load_dotenv()
data_base = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = os.environ.get('DB_PASSWD')
)

cursor_object = data_base.cursor()

cursor_object.execute("CREATE DATABASE IF NOT EXISTS botanist")

print("All done!")
