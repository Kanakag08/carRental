from dao.DBConnection import DBConnection

def createTable():
    conn=None
    try:
            conn.stmt=DBConnection.open()
            if conn:
                item='''create table if not exists Vehicle(vehicleID int primary key,
                                make varchar(20), model varchar(30), year int, dailyRate decimal(10,2),
                                status char(1), passengerCapacity int, engineCapacity int)'''
                self.execute(item)

                item ='''create table Customer(customerID int primary key,
                                firstName varchar(30), lastName varchar(30),
                                email varchar(30),phoneNumber char(10))'''
                self.execute(item)

                item=''' create table Lease(leaseID int primary key,
                                                    vehicleID int,
                                                    customerID int,
                                                    startDate date,
                                                    endDate date,
                                                    types varchar(20),
                                                    foreign key (vehicleID) references Vehicle (vehicleID),
                                                    foreign key (customerID) references Customer (customerID))'''
                self.execute(item)

                item= '''create table Payment(paymentID int primary key,
                                                        leaseID int,
                                                        paymentDate date,
                                                        Amount decimal(10,2),
                                                        foreign key (leaseID) references Lease (leaseID))'''
                self.execute(item)
                print("Table created successfully.")

    except Exception as e:
    print(f"Error: {e}")

    finally:
        if conn:
            DBConnection.close(conn)

