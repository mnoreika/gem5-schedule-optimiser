from geneticalg import GeneticAlgorithm
from tournament import Tournament
from elitism import Elitism
from singlemut import SingleMutator
from onepointcross import OnePointCrossover


# Search using a genetic algorithm
fitness = lambda x : x.count(1)
parent_selector = Tournament(3)
survival_selector = Elitism()
breeder = OnePointCrossover()
mutator = SingleMutator()

searcher = GeneticAlgorithm(10, 10, fitness, 
    parent_selector, breeder, 2, mutator, 0.3, survival_selector)

searcher.search()