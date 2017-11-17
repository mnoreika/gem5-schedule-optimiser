from random import random

class Annealer():

    def __init__(self, mutation_size, cooling_threshold):
        self.mutation_size = mutation_size
        self.temp_counter = 0
        self.mutation_rate = 1
        self.cooling_threshold = cooling_threshold

    def mutate(self, population, rate):
        mutated = []

        for i in range(self.mutation_size):
            chromosome = population[i]
            for i in range(len(chromosome)):
                rand_value = random()
                
                if rand_value <= self.mutation_rate:
                    chromosome[i] = 0 if chromosome[i] == 1 else 1

            mutated.append(chromosome)

        self.temp_counter += 1
        self.cool_down()    

        return mutated   

    def cool_down(self):
        if self.temp_counter == self.cooling_threshold:
            if self.mutation_size != 0:
                self.mutation_size -= 1
            
            if self.mutation_rate > 0:
                self.mutation_rate -= 0.1      

            self.temp_counter = 0    