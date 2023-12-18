import mysql.connector as sql
# from entity import Vehicle, Customer, Lease, Payment
from datetime import datetime

class DBConnection:
    def open(self):
        try:
            self.conn = sql.connect(host="localhost", database="carRental", user="root", password="Kagrawal@08")
            self.stmt = self.conn.cursor()
        except Exception as E:
            print(f"Database not found: {E}")

    def close(self):
        self.conn.close()