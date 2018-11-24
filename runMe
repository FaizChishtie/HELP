from src.Hospital import Hospital
from src.Patient import Patient
from src.Statistics import Statistics
import random

def tryIntExcept(trial):
    try:
        a = int(trial)
        return a
    except Exception:
        print("invalid input please try again")
        main()


def main():
    rooms = input("Enter number of rooms in hospital: ")
    rooms = tryIntExcept(rooms)
    physicians = input("Enter total number of physicians present: ")
    physicians = tryIntExcept(physicians)
    totalPatientsPerDay = input("Enter total number of patients recieved daily: ")
    totalPatientsPerDay = tryIntExcept(totalPatientsPerDay)
    days = input("Enter total number of days to gather statistics over: ")
    days = tryIntExcept(days)

    rate = totalPatientsPerDay//24

    h = Hospital(rooms,physicians)
    statistics = Statistics(h)
    for i in range(days*24):

        h.incrementWaitersTime()
        for j in range(rate):
            isFaker = False
            token = random.randint(0,6)
            if token == 1:
                isFaker = True
            h.addPatient(Patient(random.randint(1,1000),random.uniform(0,4),random.uniform(1,4),isFaker))
            h.removeNextPatients()
            h.time.increment()
        statistics.collectStats()
        statistics.returnStats()
    print("On average, the number of physicians availible every hour is: " +  str(statistics.returnStats()))



main()

