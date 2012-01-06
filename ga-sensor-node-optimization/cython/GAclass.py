# import pyevolve modules
from pyevolve import G1DBinaryString
from pyevolve import GSimpleGA
from pyevolve import Selectors
from pyevolve import Mutators
from pyevolve import DBAdapters
from pyevolve import Crossovers
from pyevolve import Consts

# import graphing module for plotting nodes
import GAgraph

# import Cython C extension for fitness function
from GAeval import eval_func

from conf import NUM_NODES
#NUM_NODES = 50
FIELD_HEIGHT = 20
FIELD_WIDTH = 20
NUM_GENERATIONS = 1000
POP_SIZE = 100
# Genetic Algorithm Probabilities
Pc = 0.75
Pm = 0.02

def run_main():
    # Define chromosome
    genome = G1DBinaryString.G1DBinaryString(NUM_NODES)

    genome.evaluator.set(eval_func)
    genome.mutator.set(Mutators.G1DBinaryStringMutatorFlip)
    genome.crossover.set(Crossovers.G1DBinaryStringXSinglePoint)

    # Initialize Genetic algorithm
    ga = GSimpleGA.GSimpleGA(genome)

    # Utilize all processors if more than one are available 
    ga.setMultiProcessing(True)

    # Set population size
    ga.setPopulationSize(POP_SIZE)

    # Set generation at which evolution pauses and interactive mode starts
    #ga.setInteractiveGeneration(500)

    # Selection
    ga.selector.set(Selectors.GTournamentSelector)
    #ga.selector.set(Selectors.GRankSelector)
    #ga.selector.set(Selectors.GUniformSelector)
    #ga.selector.set(Selectors.GRouletteWheel)

    # Set Probabilities for Genetic Algorithm
    ga.setCrossoverRate(Pc)
    ga.setMutationRate(Pm)

    ga.setElitism(True)
    ga.setElitismReplacement(NUM_NODES/4)

    ga.setGenerations(NUM_GENERATIONS)

    # Set up database for data storage and graphing with pyevolve_graph.py
    #sqlite_adapter = DBAdapters.DBSQLite(identify="ex10", resetDB=True)
    #adapter = DBAdapters.DBVPythonGraph(identify="run_01", frequency = 1)
    #ga.setDBAdapter(adapter)

    # Run genetic Algorithm
    ga.evolve(freq_stats=NUM_GENERATIONS/4)

    # Show best chromosome
    best = ga.bestIndividual()
    print 
    print "Best Chromosome:", '\n', best.getBinary()
    print "Fitness Raw Score:", best.getRawScore()
    print

    # Graph best chromosome
    i, nearest_supers = eval_func(best, graph=True)
    title = r'$%d \ Nodes$' % NUM_NODES
#    GAgraph.generate_graph(list(best.getBinary()), nearest_supers, FIELD_WIDTH, FIELD_HEIGHT, title)

