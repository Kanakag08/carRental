from util.DBConnUtil import dbConnection
def createLease():
    leaseID=int(input("Enter Lease ID: "))
    vehicleID=int(input("Enter VehicleID: "))
    customerID=int(input("Enter Customer ID: "))
    startDate=input("Enter Start Date")
    endDate=input("Enter end date")
    types=input("Enter type")
    try:
        conn,stmt=dbConnection.open()
        data=[(leaseID,vehicleID,customerID,startDate,endDate,types)]
        stmt.executemany('''insert into Lease(leaseID,vehicleID,customerID,startDate,endDate,types)
                            values(%s,%s,%s,%s,%s,%s)''',data)
        conn.commit()
        print("Data inserted Successfully")
    except Exception as E:
        print(f"ERROR DURING INSERTION {E}")
    finally:
        if conn:
            dbConnection.close(conn)