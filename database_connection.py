
import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()

def database_connection():
    try:
        connection = psycopg2.connect(
            dbname=os.getenv("db_name"),
            user=os.getenv("user"),
            password=os.getenv("password")
        )
        if connection:
            return connection
    except (Exception, psycopg2.errors) :
        return f"error occured"

        

def create_table(query):
    connection = database_connection()
    if not connection:
        return None
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("connected")
        return True
    except psycopg2.errors:
        return f"error occured:"

    finally:
        cursor.close()
        connection.close()

    


