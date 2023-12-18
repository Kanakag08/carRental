class Customer(DBConnection, Exception):
    def __init__(self):
        self.customerID = ''
        self.firstName = ''
        self.lastName = ''
        self.email = ''
        self.phoneNumber = ''

    def createCustomer(self):
        try:
            self.open()
            self.stmt.execute('''create table Customer(customerID int primary key,
                                firstName varchar(30), lastName varchar(30),
                                email varchar(30),phoneNumber char(10))''')
            print("table create sucessfully")
            self.close()
        except Exception as e:
            print(e)