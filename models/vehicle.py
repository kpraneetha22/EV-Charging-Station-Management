from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, vehicle_id, model, battery_capacity):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_capacity = battery_capacity

    @abstractmethod
    def get_vehicle_type(self):
        pass

    def display_info(self):
        print(f"Vehicle ID       : {self.vehicle_id}")
        print(f"Model            : {self.model}")
        print(f"Battery Capacity : {self.battery_capacity} kWh")
        print(f"Vehicle Type     : {self.get_vehicle_type()}")


class ElectricCar(Vehicle):

    def get_vehicle_type(self):
        return "Electric Car"


class ElectricBike(Vehicle):

    def get_vehicle_type(self):
        return "Electric Bike"


class ElectricBus(Vehicle):

    def get_vehicle_type(self):
        return "Electric Bus"