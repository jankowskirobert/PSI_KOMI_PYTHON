from Measure import Measure
import math

class DistanceStrategy(Measure):

    def calculate(self, point1, point2):
        x1 = point1.getLocationX()
        x2 = point2.getLocationX()
        y1 = point1.getLocationY()
        y2 = point2.getLocationY()
        dist = math.hypot(x2 - x1, y2 - y1) 
        return dist
