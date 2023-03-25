import random

class Dice:
    def roll(self):
        return random.randrange(1,7)
    

class DiceProbability:
    def __init__(self, n):
        self.dice = Dice()
        self.number_probability =  [0, 0, 0, 0, 0, 0]
        self.N = int(n)

    def calcProbability(self):
        for i in range(0, self.N):
            number = self.dice.roll() - 1 
            self.number_probability[ number ] = self.number_probability[ number ] + 1

    def printProbability(self):
        print("Result")
        for i in range(0, 6):
            print( i+1 , " 의 횟수 : ", self.number_probability[ i ] ,", ", i + 1, " 의 비율 : ", self.number_probability[i] / self.N)
