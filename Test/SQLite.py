import sqlite3
import sys


def printdb():
    try:
        result = theCursor.execute("SELECT ID, FName, LName, Age, Address, Salary, "
                "HireDate FROM Employees")

        for row in result:
            print(row)


    except sqlite3.OperationalError:
        print("DB Error")

db_conn =  sqlite3.connect('test.db')

print("Database Created")

theCursor = db_conn.cursor()

db_conn.execute("DROP TABLE IF EXISTS Employees")
db_conn.commit()

try:
    db_conn.execute("CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "
                    "FName TEXT NOT NULL, LName Text NOT NULL, Age INTEGER NOT NULL, "
                    "Address TEXT, Salary REAL, HireDate TEXT);")
    db_conn.commit()

except sqlite3.OperationalError:
    print("Table Couldn't Be Created")

print("Table Created")

db_conn.execute("INSERT INTO Employees (FName, LName, Age, Address, Salary, "
                "HireDate) VALUES('Derek', 'Banas', 41, '123 Main St', 50000, date('now'));")
db_conn.commit()

printdb()

db_conn.execute("UPDATE Employees SET Address = '121 Main Str' WHERE ID=1;")
db_conn.commit()
printdb()

db_conn.execute("DELETE FROM Employees WHERE ID = 1")
db_conn.commit()
printdb()

db_conn.rollback()
printdb()

db_conn.close()

print("Database Closed")