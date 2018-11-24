import random
import csv

class Patient:

    def __init__(self, _id, history, severity, faker):
        self.id = _id
        self.severity = round(severity,2)
        self.history = round(history,2)
        self.timeElapsed = 0
        self.faker = faker
        self.TRS = round(self.calculateRiskFactor(),2)

    def genOneToSix(self):
        number = random.uniform(1.0,6.0)
        return number

    def incrementTime(self):
        self.timeElapsed += 1

    def __lt__(self,other):
        return (self.TRS<other.TRS)

    def calculateRiskFactor(self):
       if self.faker == True:
            TRS = self.genOneToSix()
       else:
            TRS = 7.0 - (self.severity + self.history/2)

       return TRS

    def __repr__(self):
        return "PATIENT{ id : " + str(self.id) + ", severity: " + str(self.severity) + ", history: " + str(self.history)\
               + ", timeElapsed: " + str(self.timeElapsed) + ", Faker: " + str(self.faker) + ", TRS: " + str(self.TRS) + "}"
