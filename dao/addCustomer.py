from dao.DBConnection import DBConnection

def addCustomer(self):
    try:
        self.customerID = int(input("Enter Customer ID: "))
        self.firstName = input("Enter First Name: ")
        self.lastName = input("Enter Last Name: ")
        self.email = input("Enter email: ")
        self.phoneNumber = input("Enter Phone number: ")
        data = [(self.customerID, self.firstName, self.lastName, self.email, self.phoneNumber)]
        self.stmt.executemany('''insert into Customer(customerID,firstName,lastName,email,phoneNumber)
                                                                values(%s,%s,%s,%s,%s)''', data)
        self.conn.commit()
        print("Data inserted Sucessfully :")
        self.close()
    except Exception as e:
        print(e)