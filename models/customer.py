class Customer:

    def __init__(
        self,
        customer_id,
        name,
        phone
    ):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone

        self.vehicles = []


    def add_vehicle(self, vehicle):

        self.vehicles.append(vehicle)


    def display_customer(self):

        print(
            f"Customer ID : {self.customer_id}"
        )

        print(
            f"Name        : {self.name}"
        )

        print(
            f"Phone       : {self.phone}"
        )


    def display_vehicles(self):

        print("\nRegistered Vehicles:")


        if not self.vehicles:

            print("No vehicles registered.")

            return


        for vehicle in self.vehicles:

            print(
                f"{vehicle.vehicle_id} - "
                f"{vehicle.model} - "
                f"{vehicle.get_vehicle_type()}"
            )