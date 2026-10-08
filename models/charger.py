from abc import ABC, abstractmethod


class Charger(ABC):

    def __init__(
        self,
        charger_id,
        power
    ):
        self.charger_id = charger_id
        self.power = power

        self.is_available = True


    @abstractmethod
    def get_charger_type(self):
        pass


    @abstractmethod
    def calculate_cost(
        self,
        energy_consumed
    ):
        pass


    def reserve(self):

        if not self.is_available:

            raise Exception(
                "Charger is already occupied."
            )

        self.is_available = False


    def release(self):

        self.is_available = True


    def display_info(self):

        if self.is_available:

            status = "Available"

        else:

            status = "Occupied"


        print(
            f"Charger ID : {self.charger_id}"
        )

        print(
            f"Type       : {self.get_charger_type()}"
        )

        print(
            f"Power      : {self.power} kW"
        )

        print(
            f"Status     : {status}"
        )


class StandardCharger(Charger):

    def get_charger_type(self):

        return "Standard Charger"


    def calculate_cost(
        self,
        energy_consumed
    ):

        return energy_consumed * 8


class FastCharger(Charger):

    def get_charger_type(self):

        return "Fast Charger"


    def calculate_cost(
        self,
        energy_consumed
    ):

        return energy_consumed * 12


class SuperFastCharger(Charger):

    def get_charger_type(self):

        return "Super Fast Charger"


    def calculate_cost(
        self,
        energy_consumed
    ):

        return energy_consumed * 16