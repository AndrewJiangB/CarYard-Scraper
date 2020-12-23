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

def insertCar(make, price, year):
    cursor = connect().cursor()
    query = "INSERT INTO cars VALUES({}, {}, {});".format(make, price, year)
    cursor.execute(query)
    record = cursor.fetchone()
    return record

def checkCar(hash):
    cursor = connect().cursor()
    query = "SELECT {} FROM hashes;".format(hash)
    cursor.execute(query)
    record = cursor.fetchone()
    return record