import random
NUM_NODES = 75
FIELD_HEIGHT = 20
FIELD_WIDTH = 20

possible_coords = [ (x,y) for x in range(FIELD_WIDTH+1) for y in range(FIELD_HEIGHT+1) ]
coords = []
for i in range(NUM_NODES):
    coords.append(random.choice(possible_coords))
    possible_coords.remove(coords[i])

