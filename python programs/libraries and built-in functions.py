'''
airline="Smart Airlines"
def add(no_of_flights):
    print(no_of_flights," flights added to the fleet")
from Flights import ManageFlights                 #from packagename import modulename
ManageFlights.add(10)
import Flights.ManageFlights                      #import packagename.modulename
Flights.ManageFlights.add(10)
import Flights.Manage
import Employees.Manage
Flights.Manage.add()
Employees.Manage.add()
from Flights import Manage as FManage
from Employees import Manage as EManage
FManage.add()
EManage.add()
from Flights.Manage import add as add1
from Employees.Manage import add as add2
add1()
add2()
'''

'''
import random
x=10
y=50
print(random.randrange(x,y))
'''

'''
import math
num1=234.01
num2=6
num3=-27.01
print("The smallest integer greater than or equal to num1,",num1,":",math.ceil(num1))
print("The largest integer smaller than or equal to num1,",num1,":",math.floor(num1))
print("The factorial of num2,",num2,":", math.factorial(num2))
print("The absolute value of num3",num3,":",math.fabs(num3))
'''

'''
boarding_call="Good Evening, this is the final call to AL passengers for the flight AL 466 which is planned to take off at 8.40A.M."
if(boarding_call.startswith("Good Evening")):
    print(boarding_call.replace("Good Evening","Good Morning"))
if(boarding_call.find("AL"))>=0:
    print("Welcome to Air Lines.")
if(boarding_call.endswith("A.M.")):
    print("Passengers are requested to have their breakfast.")
a=boarding_call.split(" ")
for i in a:
    if(i.isdigit()):
        print("Flight Number is specified to the passengers.")
print("Total number of times flight service name is specified in the boarding call:",boarding_call.count("AL"))
message="Thank you all..Have a nice journey!"
print(message.upper())
print(message.lower())
'''


'''
crew_details={
    "Pilot":"Kumar",
    "Co-pilot":"Raghav",
    "Head-Strewardess":"Malini",
    "Stewardess":"Mala"
}
print("Before update:")
print("Co-pilot:",crew_details.get("Co-pilot"))
crew_details.update({"Flight Attendant":"Jane", "Co-pilot":"Henry"})
print("\nAfter update:")
print("Co-pilot:",crew_details.get("Co-pilot"))
print("Flight Attendant:",crew_details["Flight Attendant"])
'''


'''
import re
if(re.search(r"Air","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

import re
if(re.search(r"Air","airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
'''




import re
flight_details="Flight Savana Airlines a2134"
print(flight_details)
print(re.sub(r"Flight",r"Plane",flight_details))
