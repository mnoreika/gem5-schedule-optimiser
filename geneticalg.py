
from populator import Populator

class GeneticAlgorithm():

    def __init__(self, population_size, chrom_length, fitness, 
                 parent_selector, breeder, breeding_size, 
                 mutator, mutation_rate, survivor_selector):
        self.population_size = population_size
        self.chrom_length = chrom_length
        self.fitness = fitness
        self.parent_selector = parent_selector
        self.breeder = breeder
        self.breeding_size = breeding_size
        self.mutator = mutator
        self.mutation_rate = mutation_rate
        self.populator = Populator(self.population_size, self.chrom_length)
        self.generation = self.populator.gen_initial()
        self.survivor_selector = survivor_selector

    def selection(self):
        self.parents = self.parent_selector.select(self.generation, 
            self.fitness, self.breeding_size)

    def crossover(self):
        self.children = self.breeder.crossover(self.parents)

    def mutation(self):
        self.mutated = self.mutator.mutate(self.generation, self.mutation_rate)

    def survival(self):
        new_generation = self.survivor_selector.select(self.generation, 
            self.children, self.mutated)
        self.generation = new_generation

    def search(self):
        desired = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        solved = False

        h_count = 0
        gen_count = 0

        while not solved:
            for chromosome in self.generation:
                count = chromosome.count(1)

                h_count = max(count, h_count)

                if count == desired.count(1):
                    solved = True
                    print ("Solution found!")
                    break

            print ("Generation: ", gen_count, "Fitness count:", h_count)

            self.selection()
            self.crossover()
            self.mutation()
            self.survival()

            gen_count += 1