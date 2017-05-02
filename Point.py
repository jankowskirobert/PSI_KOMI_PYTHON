import math

class Point(object):
    """
    Description of Point class
    """
    def __init__(self, x = None, y = None):
        if x is None:
            self.x_location = 0
        else:
            self.x_location = x
        if y is None:
            self.y_location = 0
        else:
            self.y_location = y
        
    def getLocationX(self):
        return self.x_location

    def getLocationY(self):
        return self.y_location

    def distanceTo(self, nextPoint):
        diff_x = self.x_location - nextPoint.x_location
        diff_y = self.y_location - nextPoint.y_location
        return math.hypot(diff_x, diff_y)
    
    def __str__(self):
        return "Point at: " + str(self.x_location) + " " + str(self.y_location) 
    
