from random import randint

class Population():
    
    def __init__(self, size, chrom_length):
        self.size = size
        self.chrom_length = chrom_length

    def gen_initial(self):
    	population = []

    	for i in range(0, self.size):
    		chromosome = [randint(0, 1) for x in range(self.chrom_length)]
    		population.append(chromosome)
    	
    	return population
