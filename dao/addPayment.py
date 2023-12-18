from dao.DBConnection import DBConnection

def addPayment(self):
    try:
        self.paymentID = int(input("Enter Payment ID: "))
        self.leaseID = int(input("Enter Lease ID: "))
        self.paymentDate = input("Enter payment Date")
        self.Amount = float(input("Enter amount: "))

        data = [(self.paymentID, self.leaseID, self.paymentDate, self.Amount)]
        self.open()
        self.stmt.executemany('''insert into Payment(paymentID,leaseID,paymentDate,Amount)
                                                              values(%s,%s,%s,%s)''', data)
        self.conn.commit()
        print("Data inserted Successfully: ")
        self.close()
    except Exception as e:
        print(e)