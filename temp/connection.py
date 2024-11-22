import mysql.connector

def conn_str(dbStr="RMS"):
    try:
        conn=mysql.connector.connect(user="root", password="admin",database=dbStr)
        return conn
    except:
        print("Connection Error")
