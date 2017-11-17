import sys
from populator import Populator
from datetime import datetime

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
        self.time = str(datetime.now())
        self.result = open('results/r_' + self.time, 'a+')
        self.logger = open('logs/log_' + self.time, 'a+')

    def evaluation(self):
        eval_results = self.evaluator.calculate_fitness(self.generation) 

        # Build eval population list
        self.eval_generation = []

        for i in range(len(eval_results)):
            fitness = 1 / int(eval_results[i])
            self.eval_generation.append((self.generation[i], fitness))

        self.eval_generation = sorted(self.eval_generation, key = lambda x: x[1])

        # Store the current best chromosome
        best_file = open('results/best_' + self.time, 'w')
        best_chrom = "".join(map(str, self.eval_generation[self.population_size - 1][0]))
        best_file.write(best_chrom) 
        best_file.close()

        #Log results after each generation
        for i in range(len(eval_results)):
            self.logger.write("Individual:" + str(i) + " Time: " + 
                str(eval_results[i]) + "\n") 

        best_time = min(eval_results)
        res_message = str(self.gen_count) + "," + best_time + "\n"
        self.result.write(res_message)
        self.result.flush()

        log_message = "Generation: " + str(self.gen_count) + " Best Time : "
        log_message += best_time

        print (log_message)
        self.logger.write(log_message + "\n")
        self.logger.flush()

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
        self.gen_count = 0
        
        # Log search settings
        self.logger.write("--- Running searcher --- " +
            "\nPopulation Size: " + str(self.population_size) +
            "\nChromosome Length: " + str(self.chrom_length) + 
            "\nEvaluator: " + str(self.evaluator) +
            "\nParent Selector:" + str(self.parent_selector) +
            "\nBreeder: " + str(self.breeder) + 
            "\nBreeding Size: " + str(self.breeding_size) + 
            "\nMutator: " + str(self.mutator) + 
            "\nMutation Rate: " + str(self.mutation_rate) + 
            "\nSurvival Selector: " + str(self.survivor_selector)
            + "\n\n")

        self.result.write("generation,besttime\n")

        while self.gen_count < 100:
            self.evaluation()
            self.selection()
            self.crossover()
            self.mutation()
            self.survival()

            self.gen_count += 1
            

        self.logger.close() 
        self.result.close()
