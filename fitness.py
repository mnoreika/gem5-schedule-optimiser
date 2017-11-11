class TestFitness():

    def calculate_fitness(self, generation):
        eval_generation = []

        for chromosome in generation: 
            eval_generation.append((chromosome, chromosome.count(1)))

        eval_generation = sorted(eval_generation, key = lambda x: x[1])

        return eval_generation 