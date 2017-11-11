class Elitism():

	def select(self, eval_generation, children, mutated):
		ranked_generation = [eval_generation[i][0] for i in range(len(eval_generation))]
		new_generation = children + mutated
		new_generation += ranked_generation[len(mutated) + len(children):]
		
		return new_generation    