# EV Charging Station Management System

## Overview

The EV Charging Station Management System is a Python-based
application designed to simulate the operations of an electric
vehicle charging network.

The system manages customers, electric vehicles, charging stations,
different types of chargers, bookings, and charging sessions.

The project was developed primarily to demonstrate the practical
implementation of Object-Oriented Programming (OOP) concepts in Python.

---

## Features

- Customer management
- Electric vehicle registration
- Multiple vehicle types
- Charging station management
- Multiple charger types
- Charger availability tracking
- Charger booking
- Booking cancellation
- Charging session management
- Energy consumption tracking
- Automatic charging cost calculation
- Exception handling

---

## OOP Concepts Used

### 1. Classes and Objects

The application is divided into classes such as:

- Customer
- Vehicle
- ElectricCar
- ElectricBike
- ElectricBus
- Charger
- ChargingStation
- Booking
- ChargingSession

### 2. Inheritance

The `Vehicle` class acts as a base class for:

- ElectricCar
- ElectricBike
- ElectricBus

Similarly, `Charger` is the base class for:

- StandardCharger
- FastCharger
- SuperFastCharger

### 3. Abstraction

Abstract base classes are used to define common
behavior that child classes must implement.

Python's `ABC` and `abstractmethod` are used for this purpose.

### 4. Polymorphism

Different charger types implement the
`calculate_cost()` method differently.

For example:

- Standard Charger → ₹8/kWh
- Fast Charger → ₹12/kWh
- Super Fast Charger → ₹16/kWh

### 5. Encapsulation

Object data and operations are organized inside
their respective classes.

For example, charger availability is controlled
through methods such as:

- `reserve()`
- `release()`

### 6. Composition

A charging station contains multiple charger objects.

A customer can also have multiple registered vehicles.

### 7. Association

A booking connects:

- Customer
- Vehicle
- Charging Station
- Charger

---

## Project Structure

```text
EV_Charging_Station_Management/
│
├── main.py
├── README.md
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
└── services/
    ├── __init__.py
    ├── booking_service.py
    └── charging_service.py