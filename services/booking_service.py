from models.booking import Booking


class BookingService:

    def __init__(self):

        self.bookings = []


    def create_booking(
        self,
        booking_id,
        customer,
        vehicle,
        station,
        charger
    ):

        if not charger.is_available:

            raise Exception(
                "Selected charger is not available."
            )


        if vehicle not in customer.vehicles:

            raise Exception(
                "Vehicle is not registered to this customer."
            )


        charger.reserve()


        booking = Booking(
            booking_id,
            customer,
            vehicle,
            station,
            charger
        )


        self.bookings.append(booking)


        return booking


    def cancel_booking(
        self,
        booking
    ):

        booking.cancel()


    def display_all_bookings(self):

        if not self.bookings:

            print(
                "No bookings available."
            )

            return


        for booking in self.bookings:

            booking.display_booking()