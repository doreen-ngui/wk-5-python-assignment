from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year = year
        self._is_running = False

    @abstractmethod
    def move(self):
        pass

    def start(self):
        if not self._is_running:
            self._is_running = True
            return f"{self._brand} {self._model} has started"
        return f"{self._brand} {self._model} is already running"

    def stop(self):
        if self._is_running:
            self._is_running = False
            return f"{self._brand} {self._model} has stopped"
        return f"{self._brand} {self._model} is already stopped"

    def get_info(self):
        return {
            "Brand": self._brand,
            "Model": self._model,
            "Year": self._year,
            "Status": "Running" if self._is_running else "Stopped"
        }


class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self._fuel_type = fuel_type
        self._current_gear = "Neutral"

    def move(self):
        if not self._is_running:
            return f"{self._brand} {self._model} needs to be started first"
        return f"🚗 {self._brand} {self._model} is driving on the road"

    def change_gear(self, gear):
        valid_gears = ["Neutral", "First", "Second", "Third", "Fourth", "Fifth", "Reverse"]
        if gear in valid_gears:
            self._current_gear = gear
            return f"Changed to {gear} gear"
        return "Invalid gear"

    def get_info(self):
        info = super().get_info()
        info["Fuel Type"] = self._fuel_type
        info["Current Gear"] = self._current_gear
        return info


class Boat(Vehicle):
    def __init__(self, brand, model, year, boat_type):
        super().__init__(brand, model, year)
        self._boat_type = boat_type
        self._is_anchored = True

    def move(self):
        if not self._is_running:
            return f"{self._brand} {self._model} needs to be started first"
        if self._is_anchored:
            return f"{self._brand} {self._model} is anchored and cannot move"
        return f"⛵ {self._brand} {self._model} is sailing on the water"

    def raise_anchor(self):
        if self._is_anchored:
            self._is_anchored = False
            return "Anchor raised"
        return "Anchor is already up"

    def drop_anchor(self):
        if not self._is_anchored:
            self._is_anchored = True
            return "Anchor dropped"
        return "Anchor is already down"

    def get_info(self):
        info = super().get_info()
        info["Boat Type"] = self._boat_type
        info["Anchor Status"] = "Anchored" if self._is_anchored else "Not Anchored"
        return info


class Airplane(Vehicle):
    def __init__(self, brand, model, year, max_altitude):
        super().__init__(brand, model, year)
        self._max_altitude = max_altitude
        self._current_altitude = 0

    def move(self):
        if not self._is_running:
            return f"{self._brand} {self._model} needs to be started first"
        if self._current_altitude == 0:
            return f"{self._brand} {self._model} needs to take off first"
        return f"✈️ {self._brand} {self._model} is flying at {self._current_altitude} feet"

    def take_off(self):
        if not self._is_running:
            return f"{self._brand} {self._model} needs to be started first"
        if self._current_altitude > 0:
            return f"{self._brand} {self._model} is already in the air"
        self._current_altitude = 1000
        return f"{self._brand} {self._model} has taken off"

    def land(self):
        if self._current_altitude == 0:
            return f"{self._brand} {self._model} is already on the ground"
        self._current_altitude = 0
        return f"{self._brand} {self._model} has landed"

    def get_info(self):
        info = super().get_info()
        info["Max Altitude"] = f"{self._max_altitude} feet"
        info["Current Altitude"] = f"{self._current_altitude} feet"
        return info


# Example usage
if __name__ == "__main__":
    # Create a car
    car = Car("Toyota", "Camry", 2023, "Gasoline")
    print("\nCar Demo:")
    print(car.start())
    print(car.change_gear("First"))
    print(car.move())
    print("Car Info:", car.get_info())

    # Create a boat
    boat = Boat("Sea Ray", "Sundancer", 2022, "Motor Yacht")
    print("\nBoat Demo:")
    print(boat.start())
    print(boat.raise_anchor())
    print(boat.move())
    print("Boat Info:", boat.get_info())

    # Create an airplane
    plane = Airplane("Boeing", "737", 2021, 35000)
    print("\nAirplane Demo:")
    print(plane.start())
    print(plane.take_off())
    print(plane.move())
    print("Airplane Info:", plane.get_info()) 