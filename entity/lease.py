class Lease(DBConnection, Exception):
    def __init__(self):
        self.leaseID = ''
        self.vehicleID = ''
        self.customerID = ''
        self.startDate = ''
        self.endDate = ''
        self.types = ''

    def createLease(self):
        try:
            self.open()
            self.stmt.execute('''create table Lease(leaseID int primary key,
                                                    vehicleID int,
                                                    customerID int,
                                                    startDate date,
                                                    endDate date,
                                                    types varchar(20),
                                                    foreign key (vehicleID) references Vehicle (vehicleID),
                                                    foreign key (customerID) references Customer (customerID))''')
            print('table created sucessfully')
            self.close()
        except Exception as e:
            print(e)