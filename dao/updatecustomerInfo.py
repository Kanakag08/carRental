from dao.DBConnection import DBConnection

def updateCustInfo(self):
    try:
        self.customerID = int(input("Enter Customer ID: "))
        self.email = input("Enter new email: ")
        data = [(self.email, self.customerID)]
        self.open()
        self.stmt.executemany('''update Customer set email=%s where customerID=%s''', data)
        self.conn.commit()
        print("data uodated :")
        self.close()
    except Exception as e:
        print(e)