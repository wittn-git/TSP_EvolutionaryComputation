import random
import math

class Agent:

    def __init__(self, arg) -> None:
        self.gene = ""
        if(type(arg) == int):
            c = [i for i in range(arg)]
            for i in range(arg):
                next = c[random.randint(0, len(c)-1)]
                self.gene += str(next)
                c.remove(next)
            self.gene += self.gene[0]
        elif(type(arg) == str):
            self.gene = arg
        self.fitness = math.inf
          
    def set_fitness(self, fitness):
        self.fitness = fitness