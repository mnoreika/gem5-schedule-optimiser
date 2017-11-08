from population import Population
from random import randint
from random import random

def fitness(desired, population):
	fitness_scores = []

	for chromosome in population: 
		fitness_scores.append((chromosome, chromosome.count(1)))

	return fitness_scores	

def selection(fitness_scores, pair_number):
	 scores_sorted = sorted(fitness_scores, key = lambda x: x[1], reverse = True)

	 return scores_sorted[:pair_number * 2]


def crossover(selected):
	selected = [selected[i][0] for i in range (len(selected))]
	chrom_length = len(selected[0])
	cross_point = randint(1, chrom_length - 1)
	crossed = []

	for i in range(0, len(selected), 2):
		crossed.append(selected[i + 1][:cross_point] + selected[i][cross_point:])
		crossed.append(selected[i][:cross_point] + selected[i + 1][cross_point:])

	return crossed + selected


def mutation(chromosomes, rate):
	for chromosome in chromosomes:
		for gene in chromosome:
			rand_value = random()
		 	
			if rand_value <= rate:
				chromosome[gene] = 0 if chromosome[gene] == 1 else 1
		
	return chromosomes		


population = Population(8, 10)
generation = population.gen_initial()
desired = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
solved = False

h_count = 0
gen_count = 0

while not solved:
	for chromosome in generation:
		count = chromosome.count(1)

		h_count = max(count, h_count)

		if count == desired.count(1):
			solved = True
			print ("Solution found!")
			break

	print ("Generation: ", gen_count, "Fitness count:", h_count)

	fitness_scores = fitness(desired, generation)
	selected = selection(fitness_scores, 2)
	crossed = crossover(selected)
	new_generation = mutation(crossed, 0.10)
	generation = new_generation

	gen_count += 1