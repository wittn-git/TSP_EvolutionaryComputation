import random
import math

class Agent:

    def __init__(self, arg) -> None:
        self.gene = []
        if(type(arg) == int):
            c = [i for i in range(arg)]
            for i in range(arg):
                next = c[random.randint(0, len(c)-1)]
                self.gene.append(next)
                c.remove(next)
            self.gene.append(self.gene[0])
        elif(type(arg) == list):
            self.gene = arg
        self.fitness = math.inf
          
    def set_fitness(self, fitness):
        self.fitness = fitness