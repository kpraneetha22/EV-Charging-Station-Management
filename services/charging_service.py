from models.charging_session import ChargingSession


class ChargingService:

    def __init__(self):

        self.sessions = []


    def start_charging(
        self,
        session_id,
        booking
    ):

        if booking.status != "Confirmed":

            raise Exception(
                "Only confirmed bookings can start charging."
            )


        session = ChargingSession(
            session_id,
            booking
        )


        session.start_session()


        self.sessions.append(session)


        return session


    def stop_charging(
        self,
        session,
        energy_consumed
    ):

        session.end_session(
            energy_consumed
        )