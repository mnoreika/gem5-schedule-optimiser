from geneticalg jkimport GeneticAlgorithm
from fitness import TestFitness
from distributor import Distributor
from tournament import Tournament
from elitism import Elitism
from singlemut import SingleMutator
from multmut import MultipleMutator
from onepointcross import OnePointCrossover
from datetime import datetime
import sys

# Search using a genetic algorithm
evaluator = Distributor(25)
parent_selector = Tournament(4)
survival_selector = Elitism()
breeder = OnePointCrossover()
mutator = MultipleMutator()

searcher = GeneticAlgorithm(25, 200000, evaluator, 
    parent_selector, breeder, 4, mutator, 0.4, survival_selector)

searcher.search()