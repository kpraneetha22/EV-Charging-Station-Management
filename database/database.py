import sqlite3


class Database:

    def __init__(self, db_name="ev_charging.db"):
        self.db_name = db_name


    def connect(self):
        return sqlite3.connect(self.db_name)


    def create_tables(self):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                phone TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS vehicles (
                vehicle_id TEXT PRIMARY KEY,
                model TEXT NOT NULL,
                battery_capacity REAL NOT NULL,
                vehicle_type TEXT NOT NULL,
                customer_id TEXT,
                FOREIGN KEY (customer_id)
                REFERENCES customers(customer_id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chargers (
                charger_id TEXT PRIMARY KEY,
                charger_type TEXT NOT NULL,
                power REAL NOT NULL,
                is_available INTEGER NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bookings (
                booking_id TEXT PRIMARY KEY,
                customer_id TEXT NOT NULL,
                vehicle_id TEXT NOT NULL,
                charger_id TEXT NOT NULL,
                status TEXT NOT NULL,
                FOREIGN KEY (customer_id)
                REFERENCES customers(customer_id),
                FOREIGN KEY (vehicle_id)
                REFERENCES vehicles(vehicle_id),
                FOREIGN KEY (charger_id)
                REFERENCES chargers(charger_id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS charging_sessions (
                session_id TEXT PRIMARY KEY,
                booking_id TEXT NOT NULL,
                start_time TEXT,
                end_time TEXT,
                energy_consumed REAL,
                total_cost REAL,
                status TEXT NOT NULL,
                FOREIGN KEY (booking_id)
                REFERENCES bookings(booking_id)
            )
        """)

        connection.commit()
        connection.close()

        print("Database tables created successfully.")