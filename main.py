from dao.createTable import createTable
from dao.addLease import addLease
from dao.addCustomer import addCustomer
from dao.addPayment import addPayment
from dao.addVehicle import addVehicle
from dao.paymentHistory import paymentHistory
from dao.retriveCarInfo import retriveCarInfo
from dao.retriveCustomerInfo import retriveCustomerInfo
from dao.totalRevenue import totalRevenue
from dao.updatecustomerInfo import updateCustInfo
from dao.updateCarAvability import updateCarAvability

if __name__=="__main__":
    try:
        createTable()
        c = Customer()
        v = Vehicle()
        l = Lease()
        p = Payment()
        while (1>0):
            print("Enter 1 to Add new Vehicle: ")
            print("Enter 2 for Retreive Car Information: ")
            print("Enter 3 to Update Car Avability: ")
            print("Enter 4  to Add new Customer: ")
            print("Enter 5 to Retrive Customer Details: ")
            print("Enter 6 to Update customer details: ")
            print("Enter 7 to add New Lease: ")
            print("Enter 8 to Add new Payment: ")
            print("Enter 9 to retrive payment history: ")
            print("Enter 10 to get the total revenue: ")
            print("enter 11 to exit:")

            a = input("Enter the number: ")


            if a == '1':
                v.addVehicle()
            elif a == '2':
                v.retriveCarInfo()
            elif a == '3':
                v.UpdateCarAvailability()
            elif a == '4':
                c.addCustomer()
            elif a == '5':
                c.retriveCustomerInfo()
            elif a == '6':
                c.updateCustInfo()
            elif a == '7':
                l.addLease()
            elif a == '8':
                p.addPayment()
            elif a == '9':
                p.paymentHistory()
            elif a == '10':
                p.totalRevenue()
            elif a == '11':
                break
            else:
                print("Invalid Number or choice: ")