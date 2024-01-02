import unittest
from dao.addCar import addVehicle
from dao.listAllCars import listAllCars

class MyTestCase(unittest.TestCase):

    def testaddCar(self):
        # Create a lease
        createCar = addVehicle()
        carlist = listAllCars()
        # Check if the created lease is in the lease history
        if createCar is not None:
            for i in carlist:
                car_found = any(createCar[0][0] == i[0])
            self.assertTrue(car_found)

if __name__ == '__main__':
    unittest.main()
