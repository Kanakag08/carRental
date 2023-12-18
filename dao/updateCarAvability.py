from dao.DBConnection import DBConnection


def UpdateCarAvailability(self):
    try:
        self.vehicleID = int(input("Enter vehicle ID: "))
        self.status = input("Enter Updated Status: ")
        data = (self.status, self.vehicleID)
        self.open()
        self.stmt.execute('''update Vehicle set status=%s where vehicleID=%s''', data)
        self.conn.commit()
        print("Data updated Successfully")
        self.close()
    except Exception as e:
        print(e)