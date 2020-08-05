from datetime import datetime
import random
class Die:
    def __init__(self, numSidesP = 6, sidesP = [], weightP = []):
        if sidesP == []:
            for i in range(1,numSidesP + 1):
                sidesP.append(i)
        self.sides = sidesP
        if weightP == []:
            weightP = [1]*numSidesP
        self.weights = []
        for i in weightP:
            self.weights.append(i/sum(weightP))
        self.numSides = numSidesP
        self.roll()

    def __str__(self):
        string =  "This die has " + str(self.numSides) + " sides,"
        string += "\n"
        for i in self.sides:
            string += str(i) + "\n"
        string += "and weights, respectively,"
        string += "\n"
        for i in self.weights:
            string += str(i) + "\n"
        return string
    
    def roll(self):
        random.seed(datetime.now())
        randRoll = random.random() # in [0,1]
        mySum = 0
        i = 0
        for mass in self.weights:
            mySum += mass
            if randRoll < mySum:
                self.top = self.sides[i]
                break
            i += 1
        return self.top
    
    def getTop(self):
        return self.top
    
    def setTop(self, value):
        if value in self.sides:
            self.top = value

