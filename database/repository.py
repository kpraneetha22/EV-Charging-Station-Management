from database.database import Database


class Repository:

    def __init__(self):
        self.database = Database()

    def save_customer(self, customer):

        connection = self.database.connect()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT OR REPLACE INTO customers
            (customer_id, name, phone)
            VALUES (?, ?, ?)
        """, (
            customer.customer_id,
            customer.name,
            customer.phone
        ))

        connection.commit()
        connection.close()

    def save_vehicle(self, vehicle, customer_id):

        connection = self.database.connect()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT OR REPLACE INTO vehicles
            (vehicle_id, model, battery_capacity, vehicle_type, customer_id)
            VALUES (?, ?, ?, ?, ?)
        """, (
            vehicle.vehicle_id,
            vehicle.model,
            vehicle.battery_capacity,
            vehicle.get_vehicle_type(),
            customer_id
        ))

        connection.commit()
        connection.close()

    def save_charger(self, charger):

        connection = self.database.connect()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT OR REPLACE INTO chargers
            (charger_id, charger_type, power, is_available)
            VALUES (?, ?, ?, ?)
        """, (
            charger.charger_id,
            charger.get_charger_type(),
            charger.power,
            1 if charger.is_available else 0
        ))

        connection.commit()
        connection.close()
    def save_booking(self, booking):

        connection = self.database.connect()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT OR REPLACE INTO bookings
            (booking_id, customer_id, vehicle_id, charger_id, status)
            VALUES (?, ?, ?, ?, ?)
        """, (
            booking.booking_id,
            booking.customer.customer_id,
            booking.vehicle.vehicle_id,
            booking.charger.charger_id,
            booking.status
        ))

        connection.commit()
        connection.close()
    def save_session(self, session):

        connection = self.database.connect()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT OR REPLACE INTO charging_sessions
            (session_id, booking_id, start_time, end_time,
             energy_consumed, total_cost, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            session.session_id,
            session.booking.booking_id,
            str(session.start_time) if session.start_time else None,
            str(session.end_time) if session.end_time else None,
            session.energy_consumed,
            session.cost,
            session.status
        ))

        connection.commit()
        connection.close()
    def get_customers(self):

        connection = self.database.connect()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT customer_id, name, phone
            FROM customers
        """)

        customers = cursor.fetchall()

        connection.close()

        return customers

    def get_vehicles(self):

        connection = self.database.connect()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT vehicle_id, model, battery_capacity,
                   vehicle_type, customer_id
            FROM vehicles
        """)

        vehicles = cursor.fetchall()

        connection.close()

        return vehicles
    def get_chargers(self):

        connection = self.database.connect()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT charger_id, charger_type, power, is_available
            FROM chargers
        """)

        chargers = cursor.fetchall()

        connection.close()

        return chargers

    def get_bookings(self):

        connection = self.database.connect()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT booking_id, customer_id, vehicle_id,
                   charger_id, status
            FROM bookings
        """)

        bookings = cursor.fetchall()

        connection.close()

        return bookings

    def get_sessions(self):

        connection = self.database.connect()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT session_id, booking_id, start_time,
                   end_time, energy_consumed, total_cost, status
            FROM charging_sessions
        """)

        sessions = cursor.fetchall()

        connection.close()

        return sessions