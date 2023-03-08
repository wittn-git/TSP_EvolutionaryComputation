from agent import Agent
from operator import attrgetter
from city import City
import random
import math

class Population:
    
    def __init__(self, population_size, city_number, cities) -> None:
        self.population_size = population_size
        self.cities = cities
        self.agents = [Agent(city_number) for i in range(population_size)]

    def evolve(self):
        for agent in self.agents:
            agent.set_fitness(self.get_fitness(agent))
        new_agents = [self.get_best()]
        while(len(new_agents) < self.population_size):
            parent1, parent2 = self.choose_parent(), self.choose_parent()
            new_gene = self.breed_child(parent1, parent2)
            new_gene = self.mutate(new_gene)
            new_agents.append(Agent(new_gene))
        self.agents = new_agents
    
    def choose_parent(self):
        candidates = []
        for i in range(int(0.05*self.population_size)):
            candidates.append(self.agents[random.randint(0, self.population_size-1)])
        return min(candidates, key=attrgetter('fitness'))
    
    def breed_child(self, parent1, parent2):
        new_gene = []
        i1 = random.randint(0, len(parent1.gene)-2)
        i2 = random.randint(i1, len(parent1.gene)-2)
        segment = parent1.gene[i1:i2]
        j = 0
        while(len(new_gene) < i1):
            if parent2.gene[j] not in segment and parent2.gene[j] not in new_gene: 
                new_gene.append(parent2.gene[j])
            j += 1
        new_gene.extend(segment)
        while(len(new_gene) < len(parent1.gene)-1):
            if parent2.gene[j] not in new_gene: 
                new_gene.append(parent2.gene[j])
            j += 1
        return new_gene + [new_gene[0]]

    def mutate(self, gene):
        r = random.random()
        new_gene = gene
        if(r < 0.02):
            i1 = random.randint(1, len(gene)-2)
            i2 = random.randint(i1, len(gene)-2)
            lst = new_gene[i1:i2]
            random.shuffle(lst)
            new_gene = new_gene[:i1] + lst + new_gene[i2:]
        return new_gene

    def get_best(self):
        return min(self.agents, key=attrgetter('fitness'))

    def get_fitness(self, agent):
        return sum([City.get_distance(self.cities[int(e)], self.cities[int(agent.gene[i+1])]) for i, e in enumerate(agent.gene[0:len(agent.gene)-1])])