from math import sqrt
from coords import coords
from conf import NUM_NODES
#NUM_NODES = 50

def dist(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def eval_func(chromosome, graph=None):
    dists_to_target = []
    #for i, x in enumerate(coords[:-1:2]):
    #    dists_to_target.append(dist(x,coords[i+1],0,0))
    for x, y in coords:
        dists_to_target.append(dist(x,y,0,0))

    nearest_super = [-1 for i in chromosome]
    #for i, ivalue in enumerate(chromosome):
    #    closest = -1
    #    near = -1
    #    for j, jvalue in enumerate(chromosome):
    #        if (i != j) and (ivalue == 0) and (jvalue == 1):
    #            distance = dist(coords[i*2], coords[(i*2)+1], coords[j*2], coords[(j*2)+1])
    #            if (closest > 0 and distance < closest) or (closest == -1):
    #                closest = distance
    #                near = j
    #    if near >= 0:
    #        nearest_super[i] = near
    for i, ivalue in enumerate(chromosome):
        closest = -1
        near = -1
        for j, jvalue in enumerate(chromosome):
            if (i != j) and (ivalue == 0) and (jvalue == 1):
                distance = dist(coords[i][0], coords[i][1], coords[j][0], coords[j][1])
                if (closest > 0 and distance < closest) or (closest == -1):
                    closest = distance
                    near = j
        if near >= 0:
            nearest_super[i] = near
        
    num_super = 0
    dists_to_super = 0 
    dists_from_super = 0
    #for i, value in enumerate(chromosome):
    #    if value == 1:
    #        dists_from_super += dists_to_target[i]
    #        num_super += 1
    #    else:
    #        if nearest_super[i] != None:
    #            dists_to_super += dist(coords[i*2], coords[(i*2)+1], 
    #                                       coords[(nearest_super[i])*2], 
    #                                       coords[((nearest_super[i])*2)+1])
    for i, value in enumerate(chromosome):
        if value == 1:
            dists_from_super += dists_to_target[i]
            num_super += 1
        else:
            if nearest_super[i] != -1:
                dists_to_super += dist(coords[i][0], coords[i][1], 
                                           coords[nearest_super[i]][0], 
                                           coords[nearest_super[i]][1])
    w = 1 
    I = 0
    I = dists_to_super + dists_from_super
    fitness = ((w*sum(dists_to_target)-I) + ((1-w)*(NUM_NODES-num_super)))/100.
      
    if fitness < 0: fitness = 0
    if graph == True: return fitness, nearest_super
    return fitness

