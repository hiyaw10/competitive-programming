class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking = {}
        self.parking[1] = big
        self.parking[2] = medium
        self.parking[3] = small
        

    def addCar(self, carType: int) -> bool:
        if not self.parking.get(carType):
            return False
        else:
            self.parking[carType] -= 1
            return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)