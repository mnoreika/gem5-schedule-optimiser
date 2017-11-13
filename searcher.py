from geneticalg import GeneticAlgorithm
from fitness import TestFitness
from distributor import Distributor
from tournament import Tournament
from elitism import Elitism
from singlemut import SingleMutator
from onepointcross import OnePointCrossover


# Search using a genetic algorithm
evaluator = Distributor(25)
parent_selector = Tournament(5)
survival_selector = Elitism()
breeder = OnePointCrossover()
mutator = SingleMutator()

searcher = GeneticAlgorithm(25, 10, evaluator, 
    parent_selector, breeder, 2, mutator, 0.3, survival_selector)

searcher.search()