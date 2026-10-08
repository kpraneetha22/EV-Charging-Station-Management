class Booking:

    def __init__(
        self,
        booking_id,
        customer,
        vehicle,
        station,
        charger
    ):

        self.booking_id = booking_id

        self.customer = customer

        self.vehicle = vehicle

        self.station = station

        self.charger = charger

        self.status = "Confirmed"


    def cancel(self):

        if self.status == "Cancelled":

            raise Exception(
                "Booking is already cancelled."
            )


        self.status = "Cancelled"

        self.charger.release()


    def display_booking(self):

        print(
            "\n----- Booking Details -----"
        )

        print(
            f"Booking ID : {self.booking_id}"
        )

        print(
            f"Customer   : {self.customer.name}"
        )

        print(
            f"Vehicle    : {self.vehicle.model}"
        )

        print(
            f"Station    : {self.station.name}"
        )

        print(
            f"Charger    : {self.charger.charger_id}"
        )

        print(
            f"Status     : {self.status}"
        )