class Statistics:
    def __init__(self, hospital):
        self.hospital = hospital
        self.physiciansAvg = 0
        self.physiciansPresentAtTime = 0
        self.count = 0


    def collectStats(self):
        self.count += 1
        self.physiciansPresentAtTime = 0
        p_PD = 0
        for i in self.hospital.physiciansOccupied:
            p_PD += i[0]
        self.physiciansAvg += self.hospital.staff - p_PD

    def returnStats(self):
        return self.physiciansAvg/self.count



