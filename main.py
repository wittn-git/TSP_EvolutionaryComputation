from gui import Gui
from city import City
from population import Population
import random
from agent import Agent

def __main__():
    field_number = 50
    city_number = 70
    population_size = 2000
    generations = 500
    
    points = set()
    while len(points) < city_number:
        points.add((random.randint(2, field_number-2), random.randint(2, field_number-2)))
    cities = [City(x,y) for (x,y) in points]

    gui = Gui(field_number, cities)
    population = Population(population_size, city_number, cities)
    
    print([city.x for city in cities])
    print([city.y for city in cities])
    for i in range(generations):
        print(i)
        if(i == 3 or i == 100): print(population.get_best().gene)
        population.evolve()
        gui.draw(population.get_best())

__main__()