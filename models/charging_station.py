class ChargingStation:

    def __init__(
        self,
        station_id,
        name,
        location
    ):
        self.station_id = station_id
        self.name = name
        self.location = location

        self.chargers = []


    def add_charger(self, charger):

        self.chargers.append(charger)


    def get_available_chargers(self):

        return [
            charger
            for charger in self.chargers
            if charger.is_available
        ]


    def display_station(self):

        print(
            f"\nStation ID : {self.station_id}"
        )

        print(
            f"Name       : {self.name}"
        )

        print(
            f"Location   : {self.location}"
        )

        print(
            f"Chargers   : {len(self.chargers)}"
        )


        print("\nCharger Details:")


        for charger in self.chargers:

            charger.display_info()