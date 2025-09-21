
# This class simulates a police officer inspecting parked cars.

import math
from ParkingTicket import ParkingTicket

class PoliceOfficer:
    def __init__(self, name, badge_number):
        self.name = name
        self.badge_number = badge_number

    def inspect_car(self, parked_car, parking_meter):
        # Determine if the car has overstayed its purchased time
        illegal_minutes = (parked_car.minutes_parked - parking_meter.minutes_purchased)
        if illegal_minutes > 0:
            # Issue a parking ticket
            return ParkingTicket(
                car = parked_car,
                officer_name = self.name,
                badge_number = self.badge_number,
                illegalMinutes = illegal_minutes,
                fine = 0)
        else:
            return None