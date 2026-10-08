# EV Charging Station Management System

## Overview

The **EV Charging Station Management System** is a Python-based application that simulates the core operations of an electric vehicle charging station.

The system manages customers, electric vehicles, charging stations, different charger types, bookings, and charging sessions. It uses **Object-Oriented Programming (OOP)** for application logic and **SQLite** for persistent data storage.

The project was developed to demonstrate practical Python programming, OOP design, database integration, and basic service-layer architecture.

---

## Features

* Customer management
* Electric vehicle registration
* Multiple vehicle types
* Charging station management
* Multiple charger types
* Charger availability tracking
* Charger booking
* Booking cancellation
* Charging session management
* Energy consumption tracking
* Automatic charging cost calculation
* SQLite database persistence
* Database record retrieval
* Exception handling

---

## Technologies Used

* **Python**
* **Object-Oriented Programming (OOP)**
* **SQLite**
* **Git & GitHub**

Python's built-in `sqlite3` module is used for database operations.

---

## OOP Concepts Used

### 1. Classes and Objects

The application is divided into classes representing real-world entities such as:

* `Customer`
* `Vehicle`
* `ElectricCar`
* `ElectricBike`
* `ElectricBus`
* `Charger`
* `ChargingStation`
* `Booking`
* `ChargingSession`

---

### 2. Inheritance

The `Vehicle` class acts as a base class for:

* `ElectricCar`
* `ElectricBike`
* `ElectricBus`

Similarly, `Charger` is the base class for:

* `StandardCharger`
* `FastCharger`
* `SuperFastCharger`

---

### 3. Abstraction

Abstract base classes are used to define common behavior that child classes must implement.

Python's `ABC` and `abstractmethod` are used for abstraction.

---

### 4. Polymorphism

Different charger types implement the `calculate_cost()` method according to their charging rates.

| Charger Type       |    Cost |
| ------------------ | ------: |
| Standard Charger   |  ₹8/kWh |
| Fast Charger       | ₹12/kWh |
| Super Fast Charger | ₹16/kWh |

For example, a Fast Charger session consuming 25 kWh results in:

**25 × ₹12 = ₹300**

---

### 5. Encapsulation

Object data and operations are organized within their respective classes.

For example, charger availability is controlled through methods such as:

* `reserve()`
* `release()`

This prevents charger state from being changed arbitrarily throughout the application.

---

### 6. Composition

A charging station contains multiple charger objects.

A customer can also have multiple registered vehicles.

---

### 7. Association

A booking connects multiple objects:

* Customer
* Vehicle
* Charging Station
* Charger

A charging session is associated with a booking.

---

## SQLite Database

The application uses SQLite to persist important application data.

The database contains the following tables:

### `customers`

Stores customer information.

* Customer ID
* Name
* Phone

### `vehicles`

Stores registered electric vehicles.

* Vehicle ID
* Model
* Battery Capacity
* Vehicle Type
* Customer ID

### `chargers`

Stores charging equipment information.

* Charger ID
* Charger Type
* Power
* Availability

### `bookings`

Stores charger booking information.

* Booking ID
* Customer ID
* Vehicle ID
* Charger ID
* Booking Status

### `charging_sessions`

Stores charging session information.

* Session ID
* Booking ID
* Start Time
* End Time
* Energy Consumed
* Total Cost
* Session Status

---

## Database Architecture

The project separates database operations from the main application logic using a repository layer.

```text
Python Application
       │
       ▼
   Repository
       │
       ▼
     SQLite
       │
       ├── customers
       ├── vehicles
       ├── chargers
       ├── bookings
       └── charging_sessions
```

The `Repository` class handles database operations such as saving and retrieving records.

---

## Project Structure

```text
EV_Charging_Station_Management/
│
├── main.py
├── README.md
├── .gitignore
│
├── models/
│   ├── __init__.py
│   ├── vehicle.py
│   ├── customer.py
│   ├── charger.py
│   ├── charging_station.py
│   ├── booking.py
│   └── charging_session.py
│
├── services/
│   ├── __init__.py
│   ├── booking_service.py
│   └── charging_service.py
│
└── database/
    ├── __init__.py
    ├── database.py
    └── repository.py
```

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/kpraneetha22/EV-Charging-Station-Management.git
```

### 2. Navigate to the project

```bash
cd EV-Charging-Station-Management
```

### 3. Run the application

```bash
python main.py
```

The SQLite database file is automatically created when the application runs.

---

## Example Workflow

The application follows this basic workflow:

```text
Create Customer
      ↓
Register Electric Vehicle
      ↓
Create Charging Station
      ↓
Add Chargers
      ↓
Create Booking
      ↓
Start Charging Session
      ↓
Consume Energy
      ↓
Calculate Charging Cost
      ↓
Complete Session
      ↓
Store Data in SQLite
```

---

## Example Output

```text
Customer ID : C001
Name        : Praneetha
Phone       : 9876543210

Vehicle:
EV001 - Tata Nexon EV - Electric Car

Station:
ST001 - EV Hub - Hyderabad

Charger:
CH001 - Fast Charger - 50 kW

Booking:
B001 - Confirmed

Charging Session:
CS001
Energy Consumed : 25 kWh
Total Cost      : ₹300
Status          : Completed
```

---

## Error Handling

The application validates important operations using exception handling.

Examples include:

* Preventing a booking when a charger is unavailable
* Preventing a customer from booking a vehicle that is not registered to them
* Preventing invalid charging-session operations
* Validating energy consumption before calculating charging cost

---

## Learning Outcomes

This project demonstrates practical experience with:

* Python classes and objects
* Inheritance
* Abstraction
* Polymorphism
* Encapsulation
* Composition and association
* Exception handling
* Modular Python project structure
* Service-layer design
* SQLite database operations
* Data persistence and retrieval
* Git and GitHub version control

---

## Future Improvements

Possible future enhancements include:

* Multiple customers and stations
* Charging session history
* Database-driven customer login
* Booking history
* Revenue reports
* Charger utilization reports
* Improved command-line interface
* Data validation and input handling

---

## Author

**Kramadhati Naga Praneetha**

B.Tech – Computer Science and Engineering
