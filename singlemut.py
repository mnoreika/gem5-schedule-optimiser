from random import randint
from random import random

class SingleMutator():

    def mutate(self, population, rate):
        mutated = []
        rand_index = randint(0, len(population) - 1)

        chromosome = population[rand_index]
        for i in range(len(chromosome)):
            rand_value = random()
            
            if rand_value <= rate:
                chromosome[i] = 0 if chromosome[i] == 1 else 1

        mutated.append(chromosome)

        return mutated   