from dao.DBConnection import DBConnection

def addLease(self):
    try:
        self.leaseID = int(input("Enter Lease ID: "))
        self.vehicleID = int(input("Enter VehicleID: "))
        self.customerID = int(input("Enter Customer ID: "))
        self.startDate = input("Enter Start Date")
        self.endDate = input("Enter end date")
        self.types = input("Enter type")
        data = [(self.leaseID, self.vehicleID, self.customerID, self.startDate, self.endDate, self.types)]
        self.open()
        self.stmt.executemany('''insert into Lease(leaseID,vehicleID,customerID,startDate,endDate,types)
                                                            values(%s,%s,%s,%s,%s,%s)''', data)
        self.conn.commit()
        print("Data inserted Successfully: ")
        self.close()
    except Exception as e:
        print(e)