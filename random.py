import sys
from populator import Populator
from datetime import datetime

class Random():

	def __init__(self, population_size, chrom_length, evaluator):
		self.population_size = population_size
		self.chrom_length = chrom_length
		self.evaluator = evaluator
		self.populator = Populator(self.population_size, self.chrom_length)
		self.result = open('results/r_' + self.time, 'a+')
        self.logger = open('logs/log_' + self.time, 'a+')
        self.best_result = 999999

	def search():
		while True:
			self.generation = gen_initial()

			eval_results = self.evaluator.calculate_fitness(self.generation) 

			# Store the current best chromosome
			if 
	        best_file = open('results/best_' + self.time, 'w')
	        best_chrom = "".join(map(str, self.eval_generation[self.population_size - 1][0]))
	        best_file.write(best_chrom) 
	        best_file.close()

	        #Log results after each generation
	       	best_time = min(eval_results)

	       	if best_time < self.best_result:
	        for i in range(len(eval_results)):
	            self.logger.write("Individual:" + str(i) + " Time: " + 
	                str(eval_results[i]) + "\n") 

	        
	        res_message = str(self.gen_count) + "," + best_time + "\n"
	        self.result.write(res_message)
	        self.result.flush()

	        log_message = "Generation: " + str(self.gen_count) + " Best Time : "
	        log_message += best_time

	        print (log_message)
	        self.logger.write(log_message + "\n")
	        self.logger.flush()


