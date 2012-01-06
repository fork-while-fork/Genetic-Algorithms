import random
from conf import NUM_NODES
cdef int num_NODES = NUM_NODES

def integrity_fitness(
def battery_fitness(K):
    return sum([random.random()*K[i] for i in range(NUM_NODES) if K[i] == 1]) / sum(K)
    
def coverage_fitness(K):

def cumulative_trust_fitness(mif, mbf, mcf):
    alpha1 = alpha2 = alpha3 = 0.33333
    MIF = alpha1 * mif
    MBF = alpha2 * mbf
    MCF = alpha3 * mcf
    return MIF + MBF + MCF

def eval_func():
    mif = integrity_fitness()
    mbf = battery_fitness()
    mcf = coverage_fitness()
    return cumulative_trust_fitness(mif, mbf, mcf)
