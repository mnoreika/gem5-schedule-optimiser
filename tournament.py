from random import randint

class Tournament():

    def __init__(self, size):
        self.size = size

    def select(self, population, fitness, amount):
        parents = []
        chosen_indexes = []

        for i in range(amount):
            contestants = []

            # Conduct a tournament
            for j in range(self.size):
                found = False

                while not found: 
                    rand_index = randint(0, len(population) - 1)
                    selected = population[rand_index]
                    
                    if rand_index not in chosen_indexes:
                        found = True
                        contestants.append(selected)
                        chosen_indexes.append(rand_index)

            winner = sorted(contestants, key = lambda x: fitness(x), reverse = True)[0]
            parents.append(winner)
    
        return parents



