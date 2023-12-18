from dao.DBConnection import DBConnection

def retriveCustomerInfo(self):
    try:
        self.open()
        self.stmt.execute('''select * from Customer''')
        data = self.stmt.fetchall()
        for i in data:
            print(i)
        self.close()
    except Exception as e:
        print(e)