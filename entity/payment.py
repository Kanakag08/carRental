class Payment(DBConnection, Exception):
    def __init__(self):
        self.paymentID = ''
        self.leaseID = ''
        self.paymentDate = ''
        self.Amount = ''

    def createPayment(self):
        try:
            self.open()
            self.stmt.execute('''create table Payment(paymentID int primary key,
                                                        leaseID int,
                                                        paymentDate date,
                                                        Amount decimal(10,2),
                                                        foreign key (leaseID) references Lease (leaseID))''')
            print('table created sucessfully: ')
            self.close()
        except Exception as e:
            print(e)