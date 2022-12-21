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
        print(sum(a.fitness for a in self.agents)/self.population_size)
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
        new_gene = ""
        i1 = random.randint(0, len(parent1.gene)-2)
        i2 = random.randint(i1, len(parent1.gene)-2)
        segment1 = self.cut(parent1.gene, i1, i2)
        segment2 = self.cut(parent2.gene, i1, i2)
        new_gene = "".join(["_" for i in range(i1)]) + segment1 + "".join(["_" for i in range(i2,len(parent1.gene))])
        for i, c in enumerate(segment2):
            if c not in segment1: 
                j = parent2.gene.index(segment1[i])
                while(j >= i1 and j < i2):
                    j = parent2.gene.index(parent1.gene[j])
                new_gene = self.sub(new_gene, j, c)
        for c in parent2.gene:
            if c not in new_gene:
                new_gene = self.sub(new_gene, new_gene.index("_"), c)
        if new_gene[-1] == "_" : new_gene = self.sub(new_gene, len(new_gene)-1, new_gene[0])
        return new_gene

    def mutate(self, gene):
        r = random.random()
        new_gene = gene
        if(r < 0.02):
            i1 = random.randint(1, len(gene)-2)
            i2 = random.randint(i1, len(gene)-2)
            lst = list(self.cut(new_gene, i1, i2))
            random.shuffle(lst)
            new_gene = self.cut(new_gene, 0, i1) + "".join(lst) + self.cut(new_gene, i2, len(new_gene))
            new_gene = self.swap(new_gene, random.randint(1, len(gene)-2), random.randint(1, len(gene)-2))
        return new_gene
    
    def swap(self, s, i, j):
        lst = list(s)
        lst[i], lst[j] = lst[j], lst[i]
        return ''.join(lst)
    
    def cut(self, s, i, j):
        lst = list(s)
        lst = lst[i:j]
        return ''.join(lst)
    
    def sub(self, s, i, a):
        lst = list(s)
        lst[i] = a
        return ''.join(lst)

    def get_best(self):
        return min(self.agents, key=attrgetter('fitness'))
    
    def draw(self, agent):
        for i, e in enumerate(agent.gene[0:len(agent.gene)-1]):
            City.draw_egde(self.cities[int(e)], self.cities[int(agent.gene[i+1])])
    
    def get_fitness(self, agent):
        return sum([City.get_distance(self.cities[int(e)], self.cities[int(agent.gene[i+1])]) for i, e in enumerate(agent.gene[0:len(agent.gene)-1])])