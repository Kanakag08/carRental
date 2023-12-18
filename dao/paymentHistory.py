from dao.DBConnection import DBConnection

def paymentHistory(self):
    try:
        customerID = int(input("Enter customer ID"))
        self.open()
        self.stmt.execute(''' select P.paymentID, P.leaseID, P.paymentDate, P.Amount
                                        from Payment P
                                        inner join Lease L ON P.leaseID = L.leaseID
                                        where L.customerID = %s''', (customerID,))
        paymentHistory = self.stmt.fetchall()
        if paymentHistory:
            print(f"Payment History for Customer ID {customerID}:")
            for payment in paymentHistory:
                paymentID, leaseID, paymentDate, Amount = payment
                print(
                    f"Payment ID: {paymentID}, Lease ID: {leaseID}, Payment Date: {paymentDate}, Amount: {Amount}")
        else:
            raise CustomerNotFoundException(f"No payment history found for Customer ID {customerID}")
    except CustomerNotFoundException as CN:
        print(CN)
    except Exception as e:
        print(e)
    self.close()