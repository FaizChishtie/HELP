class Time:
    def __init__(self):
        self.daysPassed = 0
        self.time = 0
        self.severeTotal = 0
        self.moderateTotal = 0
        self.mildTotal = 0
        self.fakerTotal = 0

    def increment(self):
        self.time += 1
        if(self.dayOver()):
            self.daysPassed += 1
            self.time = 0

    def dayOver(self):
        return self.time == 24

    def returnAverageOverDays(self):
        timePassed = self.daysPassed*24 + self.time
        return (self.severeTotal//timePassed, self.moderateTotal//timePassed, self.mildTotal//timePassed, self.fakerTotal//timePassed)

