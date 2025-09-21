
# This class simulates a parking ticket issued to a car.

import math

class ParkingTicket:
    def __init__(self, car, officer_name, badge_number, illegalMinutes, fine):
        self.car = car
        self.officer_name = officer_name
        self.badge_number = badge_number
        self.illegalMinutes = illegalMinutes
        self.fine = self.calculate_fine()

    def calculate_fine(self):
        hours = math.ceil(self.illegalMinutes / 60)
        if hours <= 1:
            return 25.00
        else:
            return 25.00 + (hours -1) * 10.00

    def __str__(self):
        return (
            f"Parking Ticket\n\n"
            f"Car: {self.car}\n"
            f"Officer: {self.officer_name}\n"
            f"Badge Number: {self.badge_number}\n"
            f"Illegally Parked: {self.illegalMinutes}\n"
            f"Fine: ${self.fine:.2f}")



