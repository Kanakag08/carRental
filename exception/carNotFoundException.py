from exception.DBConnection import DBConnection

class CarNotFoundException(Exception):
    def __init__(self, car_id):
        super().__init__(f"Car with ID {vehicle_id} not found in the database")
