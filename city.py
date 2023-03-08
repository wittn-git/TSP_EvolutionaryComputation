import math

class City:

    def __init__(self, x, y) -> None:
        self.x, self.y = x, y
    
    @staticmethod
    def get_distance(city1, city2):
        return math.sqrt((city1.x-city2.x)**2 + (city1.y-city2.y)**2)