'''
airline="Smart Airlines"
def add(no_of_flights):
    print(no_of_flights," flights added to the fleet")
from Flights import ManageFlights #from packagename import modulename
ManageFlights.add(10)
import Flights.ManageFlights #import packagename.modulename
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
