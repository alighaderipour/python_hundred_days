# ? an object
# * what an object has? 1. (attributes => variables ) and 2. what it does (methods)
# * an object is a real world thing that has something and do something
# ? consider a class as a blueprint, from a class we can make as many object we want


class Car:
    def __init__(self, make, model, year, color, mileage=0):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

    def drive(self, distance):
        """Simulate driving the car a certain distance."""
        self.mileage += distance
        print(f"Driven {distance} miles. Total mileage is now {self.mileage} miles.")

    def repaint(self, new_color):
        """Change the color of the car."""
        old_color = self.color
        self.color = new_color
        print(f"The car has been repainted from {old_color} to {new_color}.")

    def display_info(self):
        """Display full information about the car."""
        print(
            f"Car Information: {self.year} {self.make} {self.model}, Color: {self.color}, Mileage: {self.mileage} miles"
        )


# Example usage:
my_car = Car(make="Toyota", model="Corolla", year=2020, color="Red")
my_car.display_info()
my_car.drive(100)
my_car.repaint("Blue")
my_car.display_info()
