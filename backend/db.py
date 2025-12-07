import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="recipe_app_user",
            password="Kz8gnHfufP4b",
            database="recipebox"
        )
        return conn
    except Error as e:
        print("Database connection error:", e)
        return None


if __name__ == "__main__":
    conn = get_db_connection()
    if conn:
        print("Connected successfully!")
        conn.close()
    else:
        print("Connection failed.")
