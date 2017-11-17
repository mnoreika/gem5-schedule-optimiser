from random import randint
from random import random

class MultipleMutator():

    def mutate(self, population, rate):
        mutated = []

        for i in range(int(len(population) / 2)):
            chromosome = population[i]
            for i in range(len(chromosome)):
                rand_value = random()
                
                if rand_value <= rate:
                    chromosome[i] = 0 if chromosome[i] == 1 else 1

            mutated.append(chromosome)

        return mutated   
