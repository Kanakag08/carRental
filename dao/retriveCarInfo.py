from dao.DBConnection import DBConnection


def retriveCarInfo(self):
    try:
        self.open()
        self.stmt.execute('''select *  from Vehicle''')
        data = self.stmt.fetchall()
        for i in data:
            print(i)
        self.close()
    except Exception as e:
        print(e)