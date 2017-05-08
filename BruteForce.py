import math
import itertools
class BruteForceMethod(object):

    def __init__(self, listOfPoint, strategy):
        self.listOfPoint = listOfPoint
        self.strategy = strategy

    def resolveProblem(self):
        self.permutations = list(itertools.permutations(self.listOfPoint, len(self.listOfPoint)))
        result = float("Inf")
        path = -1
        #print(list(self.permutations))
        listLen = len(self.permutations)
        print(listLen)
        for i in range(0, listLen):            
            sumByStrategy = 0
            subListLen = len(self.permutations[i])
            for j in range(0, subListLen-1):
                sumByStrategy += self.strategy.calculate(self.permutations[i][j], self.permutations[i][j+1])
            print(sumByStrategy)
            if sumByStrategy < result:
                result = sumByStrategy
                path = i
        print("BR: " + str(result) + " " + str(path))
        print("Path:" + str(self.permutations[path]))


