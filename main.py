from database import repository
from database.database import Database
from database.repository import Repository
from models import booking
from models.vehicle import ElectricCar
from models.customer import Customer
from models.charger import FastCharger, StandardCharger
from models.charging_station import ChargingStation

from services.booking_service import BookingService
from services.charging_service import ChargingService

def main():

    database = Database()
    database.create_tables()
    repository = Repository()
    # -----------------------------
    # Create Customer
    # -----------------------------

    customer = Customer(
        "C001",
        "Praneetha",
        "9876543210"
    )
    repository.save_customer(customer)

    # -----------------------------
    # Create Vehicle
    # -----------------------------

    car = ElectricCar(
        "EV001",
        "Tata Nexon EV",
        40
    )

    customer.add_vehicle(car)
    repository.save_vehicle(car, customer.customer_id)

    # -----------------------------
    # Create Charging Station
    # -----------------------------

    station = ChargingStation(
        "ST001",
        "EV Hub",
        "Hyderabad"
    )


    # -----------------------------
    # Create Chargers
    # -----------------------------

    charger1 = FastCharger(
        "CH001",
        50
    )

    charger2 = StandardCharger(
        "CH002",
        22
    )


    # -----------------------------
    # Add Chargers to Station
    # -----------------------------

    station.add_charger(charger1)
    station.add_charger(charger2)
    repository.save_charger(charger1)
    repository.save_charger(charger2)


    # -----------------------------
    # Display Customer
    # -----------------------------

    customer.display_customer()
    customer.display_vehicles()


    # -----------------------------
    # Display Charging Station
    # -----------------------------

    station.display_station()


    # -----------------------------
    # Create Booking
    # -----------------------------

    booking_service = BookingService()

    booking = booking_service.create_booking(
        "B001",
        customer,
        car,
        station,
        charger1
    )
    repository.save_booking(booking)

    booking.display_booking()


    # -----------------------------
    # Start Charging
    # -----------------------------

    charging_service = ChargingService()

    session = charging_service.start_charging(
        "CS001",
        booking
    )

    repository.save_session(session)
    session.display_session()


    # -----------------------------
    # End Charging
    # -----------------------------

    charging_service.stop_charging(
        session,
        25
    )

    repository.save_session(session)
    session.display_session()


    # -----------------------------
    # Final Charger Status
    # -----------------------------

    print("\nFinal Charger Status:")

    charger1.display_info()


# -----------------------------
# Program Entry Point
# -----------------------------

if __name__ == "__main__":
    main()