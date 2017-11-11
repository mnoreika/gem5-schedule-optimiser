class Elitism():

	def evaluate(self, population):
	    fitness_scores = []

	    for chromosome in population: 
	        fitness_scores.append((chromosome, chromosome.count(1)))

	    fitness_scores = sorted(fitness_scores, key = lambda x: x[1])   

	    return [fitness_scores[i][0] for i in range(len(fitness_scores))]

	def select(self, population, children, mutated):
		ranked_generation = self.evaluate(population)

		new_generation = children + mutated
		new_generation += ranked_generation[len(mutated) + len(children):]
		
		return new_generation    