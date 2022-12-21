from gui import Gui
from city import City
from population import Population
import random
from agent import Agent


def loop(cities, gui, population):
    for city1 in cities:
        city1.draw_city()
    population.evolve()
    population.draw(population.get_best())

def __main__():
    field_number = 25
    city_number = 15
    population_size = 150
    gui = Gui(field_number)
    cities = [City(random.randint(0, field_number-1), random.randint(0, field_number-1), gui) for i in range(city_number)]
    population = Population(population_size, city_number, cities)
    gui.start(loop, (cities, gui, population))

__main__()