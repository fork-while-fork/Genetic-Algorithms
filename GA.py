from pyevolve import G1DBinaryString
from pyevolve import GSimpleGA
from pyevolve import Selectors
from pyevolve import Mutators
from pyevolve import DBAdapters

from math import sqrt 
import random 
import copy

import coords as c
import GAgraph

NUM_NODES = 50
FIELD_WIDTH = 20
FIELD_HEIGHT = 20
coords = [(1,3), (1,8), (2,1), (2,3), (2,7),
             (3,6), (3,8), (4,3), (5,6), (5,7),
             (6,3), (6,4), (6,6), (7,3), (7,7)]

coords = c.coords
NEAREST_SUPERS = []

# This function is the evaluation function, we want
# to give high score to more zero'ed chromosomes
def dist(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def eval_func(chromosome, graph=None):
    dists_to_target = []
    for x, y in coords:
        dists_to_target.append(dist(x,y,0,0))

    nearest_super = [None for i in range(len(chromosome))]
    for i in range(len(chromosome)):
        closest = -1
        near = -1
        for j in range(len(chromosome)):
            if (i != j) and (chromosome[i] == 0) and (chromosome[j] == 1):
                distance = dist(coords[i][0], coords[i][1], coords[j][0], coords[j][1])
                if (closest > 0 and distance < closest) or (closest == -1):
                    closest = distance
                    near = j
        if near >= 0:
            nearest_super[i] = near
        
    assert len(nearest_super) == len(coords)
    dists_to_super = []
    dists_from_super = []
    num_super = 0
    for i, value in enumerate(chromosome):
        if value == 1:
            dists_from_super.append(dists_to_target[i])
            num_super += 1
        else:
            if nearest_super[i] != None:
                dists_to_super.append(dist(coords[i][0], coords[i][1], 
                                           coords[nearest_super[i]][0], 
                                           coords[nearest_super[i]][1]))
    num_super = 0
    for i in chromosome:
        if i == 1:
            num_super += 1

    w = 1 
    I = 0
    I = sum(dists_to_super) + sum(dists_from_super)
    fitness = (w*(sum(dists_to_target)-I) + ((1-w)*(NUM_NODES-num_super)))/100.
      
    if fitness < 0: fitness = 0
    if graph == True: 
        return fitness, nearest_super
    ##assert fitness > 0
    return fitness

#def chromosomes_init(genome):
#    genome.genomeString = [random.choice((0,1)) for i in range(NUM_NODES)]
    
# Genome instance
genome = G1DBinaryString.G1DBinaryString(NUM_NODES)
#print genome

# The evaluator function (objective function)
genome.evaluator.set(eval_func)
genome.mutator.set(Mutators.G1DBinaryStringMutatorFlip)
#genome.initializator.set(chromosomes_init)

# Genetic Algorithm Instance
ga = GSimpleGA.GSimpleGA(genome)

ga.selector.set(Selectors.GRankSelector)
ga.setCrossoverRate(0.75)
ga.setMutationRate(0.02)
ga.setElitism(True)

ga.setGenerations(100)
ga.terminationCriteria.set(GSimpleGA.ConvergenceCriteria)

sqlite_adapter = DBAdapters.DBSQLite(identify="ex10", resetDB=True)
ga.setDBAdapter(sqlite_adapter)

# Do the evolution, with stats dump
# frequency of 10 generations
ga.evolve(freq_stats=10)

# Best individual
best = ga.bestIndividual()
#print best
i, nearest_supers = eval_func(best, graph=True)
title = r'$Rank \ Selection$'
GAgraph.generate_graph(list(best.getBinary()), nearest_supers, FIELD_WIDTH, FIELD_HEIGHT, coords, title)
