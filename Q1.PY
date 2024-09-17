import numpy as np
def reservations(idd,passenger_records):
    for hi in passenger_records:
        if hi[0]==idd:
            print(hi[1])

def availability(passid,flightSchedule,numbus,numecon):
    for hi in flightSchedule:
        if hi[0]==passid:
            hi[4]=numbus
            hi[5]=numecon

def maxmin(schedule,record):
    reservation_count = {flight[0]: 0 for flight in schedule} #count intialize karo
    for passenger in record:
        for reservation in passenger[2]:
            flight_number = reservation.split(':')[0]
            if flight_number in reservation_count:
                reservation_count[flight_number] += 1
    max_flight = max(reservation_count, key=reservation_count.get)
    min_flight = min(reservation_count, key=reservation_count.get)
    print(max_flight)
    print(min_flight)

def find_fully_booked_flights(flightSchedule):
    fully_booked_flights = []
    for flight in flightSchedule:
        if int(flight[4]) == 0 and int(flight[5]) == 0:
            fully_booked_flights.append(flight[0])
    print(fully_booked_flights)


flightSchedule = np.array([[1, 'A', 'B', '10:00', 10, 50],[2, 'B', 'C', '14:00', 5, 20],[3, 'A', 'C', '06:00', 0, 0],])
passenger_records = np.array([[51, 'Harsh', 1],[52, 'Tyagi', 2],[53, 'Gillu', 1],])

reservations('52',passenger_records)
print(flightSchedule)
availability('2',flightSchedule,'3','4')
print(flightSchedule)
find_fully_booked_flights(flightSchedule)



