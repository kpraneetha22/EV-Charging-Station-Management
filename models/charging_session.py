from datetime import datetime


class ChargingSession:

    def __init__(
        self,
        session_id,
        booking
    ):

        self.session_id = session_id

        self.booking = booking

        self.start_time = None

        self.end_time = None

        self.energy_consumed = 0

        self.cost = 0

        self.status = "Not Started"


    def start_session(self):

        if self.status != "Not Started":

            raise Exception(
                "Charging session cannot be started."
            )


        self.start_time = datetime.now()

        self.status = "Charging"


    def end_session(
        self,
        energy_consumed
    ):

        if self.status != "Charging":

            raise Exception(
                "Charging session is not active."
            )


        if energy_consumed <= 0:

            raise ValueError(
                "Energy consumed must be greater than zero."
            )


        self.energy_consumed = energy_consumed

        self.end_time = datetime.now()


        self.cost = (
            self.booking.charger.calculate_cost(
                energy_consumed
            )
        )


        self.booking.charger.release()

        self.status = "Completed"


    def display_session(self):

        print(
            "\n----- Charging Session -----"
        )

        print(
            f"Session ID      : {self.session_id}"
        )

        print(
            f"Booking ID      : {self.booking.booking_id}"
        )

        print(
            f"Start Time      : {self.start_time}"
        )

        print(
            f"End Time        : {self.end_time}"
        )

        print(
            f"Energy Consumed : {self.energy_consumed} kWh"
        )

        print(
            f"Total Cost      : ₹{self.cost}"
        )

        print(
            f"Status          : {self.status}"
        )