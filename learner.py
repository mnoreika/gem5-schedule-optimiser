from population import Population
from tournament import Tournament
from random import randint
from random import random

def evaluation(population, fitness):
	fitness_scores = []

	for chromosome in population: 
		fitness_scores.append((chromosome, chromosome.count(1)))

	fitness_scores = sorted(fitness_scores, key = lambda x: x[1])	

	return [fitness_scores[i][0] for i in range(len(fitness_scores))]

# def selection(fitness_scores, selector, fitness):
# 	 selector.select(fitness_scores)

# 	 return scores_sorted[:2]

def fitness(chromosome):
	return chromosome.count(1)


def crossover(parents):
	chrom_length = len(parents[0])
	cross_point = randint(1, chrom_length - 1)
	children = []
	
	children.append(parents[1][:cross_point] + parents[0][cross_point:])
	children.append(parents[0][:cross_point] + parents[1][cross_point:])

	return children


def mutation(chromosomes, rate):
	rand_index = randint(0, len(chromosomes) - 1)

	chromosome = chromosomes[rand_index]
	
	for gene in chromosome:
		rand_value = random()
	 	
		if rand_value <= rate:
			chromosome[gene] = 0 if chromosome[gene] == 1 else 1
		
	return chromosome	


population = Population(14, 10)
generation = population.gen_initial()
desired = [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
solved = False

h_count = 0
gen_count = 0

selector = Tournament(3)

while not solved:
	for chromosome in generation:
		count = chromosome.count(1)

		h_count = max(count, h_count)

		if count == desired.count(1):
			solved = True
			print ("Solution found!")
			break

	print ("Generation: ", gen_count, "Fitness count:", h_count)

	parents = selector.select(generation, fitness, 2)
	children = crossover(parents)
	eval_population = evaluation(generation, fitness)
	mutated = mutation(eval_population, 0.3)

	new_generation = children + eval_population[3:]
	new_generation.append(mutated)
	generation = new_generation

	gen_count += 1