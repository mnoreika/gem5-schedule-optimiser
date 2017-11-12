import sys
from populator import Populator

class GeneticAlgorithm():

    def __init__(self, population_size, chrom_length, evaluator, 
                 parent_selector, breeder, breeding_size, 
                 mutator, mutation_rate, survivor_selector):
        self.population_size = population_size
        self.chrom_length = chrom_length
        self.evaluator = evaluator
        self.parent_selector = parent_selector
        self.breeder = breeder
        self.breeding_size = breeding_size
        self.mutator = mutator
        self.mutation_rate = mutation_rate
        self.populator = Populator(self.population_size, self.chrom_length)
        self.generation = self.populator.gen_initial()
        self.survivor_selector = survivor_selector

    def evaluation(self):
        self.eval_generation = self.evaluator.calculate_fitness(self.generation) 

    def selection(self):
        self.parents = self.parent_selector.select(self.eval_generation, 
            self.breeding_size)

    def crossover(self):
        self.children = self.breeder.crossover(self.parents)

    def mutation(self):
        self.mutated = self.mutator.mutate(self.generation, self.mutation_rate)

    def survival(self):
        new_generation = self.survivor_selector.select(self.eval_generation, 
            self.children, self.mutated)

        self.generation = new_generation

    def search(self):
        gen_count = 0
        logger = open('log.txt', 'a+')

        logger.write("generation,hfitness\n")

        while gen_count < 10:
            self.evaluation()
            self.selection()
            self.crossover()
            self.mutation()
            self.survival()

            log_message = str(gen_count) + "," + str(self.eval_generation[self.population_size - 1][1]) + "\n"
            logger.write(log_message)

            print ("Generation: ", gen_count, 
                "Highest Fitness:", self.eval_generation[self.population_size - 1][1])

            gen_count += 1
            

        logger.close()     