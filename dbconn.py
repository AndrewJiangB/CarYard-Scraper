import psycopg2

def connect():
    conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="mango")
    return conn

def getCars():
    cursor = connect().cursor()
    cursor.execute("SELECT * FROM cars;")
    record = cursor.fetchone()
    return record