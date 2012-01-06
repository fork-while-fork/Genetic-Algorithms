from pyevolve import G1DList
from pyevolve import GSimpleGA
from pyevolve import Consts
from pyevolve import Selectors
from pyevolve import Initializators
from pyevolve import Mutators
from pyevolve import Crossovers

from PIL import Image

image = Image.open("lena64.bmp")
image_pixels = []
for i in range(image.size[0]): 
    for j in range(image.size[1]):
        image_pixels.append(image.getpixel((i,j)))

n = 0
o = 0
def callback(ga_engine):
    global n
    global o
    if o % 10 == 0:
        generation = ga_engine.getCurrentGeneration()
        current_best = ga_engine.bestIndividual()
        im = Image.new(image.mode, image.size)
        i = 0
        j = 0
        for pixel in current_best:
            im.putpixel((i, j), pixel)
            j += 1
            if j == image.size[1]:
                i += 1
                j = 0
        im.save("./images/image%d.bmp" % n)
        n += 1
    o += 1
    return False

def fitness(genome):
    return sum(abs(a-b) for a, b in zip(genome, image_pixels))

def main():
    genome = G1DList.G1DList(len(image_pixels))
    genome.setParams(rangemin=min(image_pixels),
                     rangemax=max(image_pixels),
                     bestrawscore=0.00)
 
    genome.initializator.set(Initializators.G1DListInitializatorInteger)
    genome.mutator.set(Mutators.G1DListMutatorIntegerRange)
    genome.evaluator.set(fitness)
 
    ga = GSimpleGA.GSimpleGA(genome)
    ga.stepCallback.set(callback)
    ga.setMinimax(Consts.minimaxType["minimize"])
    ga.terminationCriteria.set(GSimpleGA.RawScoreCriteria)
    ga.selector.set(Selectors.GRankSelector)
    ga.setPopulationSize(20)
    ga.setMutationRate(0.005)
    ga.setCrossoverRate(.75)
    ga.setGenerations(5000)
    ga.evolve(freq_stats=100)

if __name__ == "__main__":
    main()
