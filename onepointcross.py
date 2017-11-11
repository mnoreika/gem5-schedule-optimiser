from random import randint

class OnePointCrossover():

    def crossover(self, parents):
        cross_point = randint(1, len(parents[0]) - 1)
        children = []
        
        children.append(
            parents[1][:cross_point] + parents[0][cross_point:])
        children.append(
            parents[0][:cross_point] + parents[1][cross_point:])

        return children
