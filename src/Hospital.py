import queue as Q
from src.Patient import Patient
from src.Time import Time

class Hospital:
    def __init__(self, rooms, staff):
        self.time = Time()
        self.isActive = True
        self.rooms = rooms
        self.staff = staff
        self.physicianCount = staff
        self.physiciansOccupied = []
        self.q = Q.PriorityQueue() #lower priority is higher

    def incrementTime(self):
        self.time.increment()

    def addPatient(self, patient):
        self.q.put((patient.TRS, patient))

    def getSize(self):
        return self.q.qsize()

    def isEmpty(self):
        return self.getSize()==0

    def isActive(self):
        return self.isActive

    def printQueue(self):
        print(self.q.queue)

    def removeNextPatients(self):
        if not self.isEmpty():
            _p = self.q.get()
            patient = _p[1]
            numPhysicians = self.patientToPhysician(patient.TRS)
            while self.physicianCount - numPhysicians >= 0 and self.rooms > 0:
                self.processPatient(patient, numPhysicians)
                if not self.q.empty():
                    patient = self.q.get()[1]


    def patientToPhysician(self,TRS):
        staff=0
        if TRS>=5 and TRS<=6:
            staff=1
        elif TRS>=3 and TRS<5:
            staff=2
        elif TRS>=1 and TRS<3:
            staff=4
        return staff

    def processPatient(self, patient, numPhysicians):
        self.physicianCount -= numPhysicians
        self.rooms -= 1
        if patient.faker:
            return 1 #patient was a faker
        timeSpent = numPhysicians
        if timeSpent <= 2:
            timeSpent += 1
        self.physiciansOccupied.append([numPhysicians,timeSpent])
        return timeSpent

    def decrementTimeRemainingPhysicians(self):
        for i in self.physiciansOccupied:
            i[1] -= 1
            if i[1] >= 0:
                self.physicianCount += i[0]


    def printTime(self):
        print(self.time.time)

    def incrementWaitersTime(self):
        if not self.isEmpty():
            l = list(self.q.queue)
            for i in l:
                i[1].incrementTime()
                self.incrementWaitingTimeBasedOnSeverity(i[1].TRS, i[1].faker)
            self.q.queue.clear()
            for i in l:
                self.addPatient(i[1])

    def incrementWaitingTimeBasedOnSeverity(self,TRS, faker):
        if faker:
            self.time.fakerTotal += 1
            return
        if TRS>=5 and TRS<=6:
            self.time.mildTotal += 1
        elif TRS>=3 and TRS<5:
            self.time.moderateTotal += 1
        elif TRS>=1 and TRS<3:
            self.time.severeTotal += 1











