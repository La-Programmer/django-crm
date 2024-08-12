import mysql.connector


data_base = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'j1u2s3t4i5n6' 
)

cursor_object = data_base.cursor()

cursor_object.execute("CREATE DATABASE botanist")

print("All done!")
