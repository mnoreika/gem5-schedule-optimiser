class GeneticAlgorithm():

	def __init__(self, population_size, chrom_length, fitness, 
				 selector, mutation_rate, breeding_size, survivor_selector):
		self.population_size = population_size
		self.chrom_length = chrom_length
		self.fitness = fitness
		self.selector = selector
		self.mutation_rate = mutation_rate
		self.populator = Populator(self.population_size, self.chrom_length)
		self.generation = self.populator.gen_initial()
		self.survivor_selector = survivor_selector
		self.mutated = []

	def selection(self):
		self.parents = selector.select(self.generation, 
			self.fitness, self.breeding_size)

	def crossover(self):
	    cross_point = randint(1, self.chrom_length - 1)
	    children = []
	    
	    children.append(self.parents[1][:cross_point] + self.parents[0][cross_point:])
	    children.append(self.parents[0][:cross_point] + self.parents[1][cross_point:])

	    return children	

	def mutation(self):
	    rand_index = randint(0, self.population_size - 1)

	    chromosome = self.population[rand_index]
	    for i in range(self.chrom_length):
	        rand_value = random()
	        
	        if rand_value <= self.rate:
	            chromosome[i] = 0 if chromosome[i] == 1 else 1

	    mutated.append(chromosome)   

	def survival(self):
		self.

	def search(self):
