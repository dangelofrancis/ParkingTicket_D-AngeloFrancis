# TITLE: Parking Ticket Simulation
# FILE NAME: ParkingTicket_D_AngeloFrancis.py
# DATE: 9/21/2025
# PROGRAMMER: D'Angelo Francis
# REQUIREMENTS: Simulate police officer issuing parking tickets

from ParkingMeter import ParkingMeter
from ParkedCar import ParkedCar
from PoliceOfficer import PoliceOfficer
from ParkingTicket import ParkingTicket


################
#  SCENARIO 1  #
################

print("SCENARIO 1")

car = ParkedCar("Toyota", "Camry", "Red", "XYZ123", 30)
meter = ParkingMeter(40)
officer = PoliceOfficer("John Doe", "5678")
ticket = officer.inspect_car(car, meter)

if ticket:
    print(ticket)
else:
    print("No violation. Car is parked legally.\n")

################
#  SCENARIO 2  #
################

print("SCENARIO 2")

car = ParkedCar("Honda", "Accord", "Blue", "ABC987", 70)
meter = ParkingMeter(60)
officer = PoliceOfficer("Jane Smith", "1234")
ticket = officer.inspect_car(car, meter)

if ticket:
    print(ticket)
else:
    print("No violation. Car is parked legally.\n")

################
#  SCENARIO 3  #
################

print("SCENARIO 3")

car = ParkedCar("Ford", "Mustang", "Black", "LMN465", 190)
meter = ParkingMeter(60)
officer = PoliceOfficer("James Brown", "4321")
ticket = officer.inspect_car(car, meter)

if ticket:
    print(ticket)
else:
    print("No violation. Car is parked legally.\n")

