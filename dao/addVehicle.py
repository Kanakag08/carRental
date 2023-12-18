from dao.DBConnection import DBConnection

def addVehicle(self):
    try:
        self.vehicleID = int(input("Enter VehicleID: "))
        self.make = input("Enter make: ")
        self.model = input("Enter model")
        self.year = int(input("Enter year"))
        self.dailyRate = float(input("Enter daily Rate: "))
        self.status = input("Enter status: ")
        self.passengerCapacity = int(input("Enter passenger capacity: "))
        self.engineCapacity = int(input("Enter engine capacity: "))
        data = [(self.vehicleID, self.make, self.model, self.year, self.dailyRate, self.status,
                 self.passengerCapacity, self.engineCapacity)]
        self.open()
        self.stmt.executemany('''insert into Vehicle(vehicleID,
                                                              make,
                                                              model,
                                                              year,
                                                              dailyRate,
                                                              status,
                                                              passengerCapacity,
                                                              engineCapacity)
                                                              values(%s,%s,%s,%s,%s,%s,%s,%s)''', data)
        self.conn.commit()
        print("Data inserted sucessfully :")
        self.close()
    except Exception as e:
        print(e)