from dao.DBConnection import DBConnection

def totalRevenue(self):
    try:
        self.open()
        self.stmt.execute('''select sum(Amount) from Payment''')
        totalRevenue = self.stmt.fetchone()[0]
        if totalRevenue is not None:
            print(f"Total revenue is {totalRevenue}")
        else:
            print("payment not found: ")
    except Exception as e:
        print(e)