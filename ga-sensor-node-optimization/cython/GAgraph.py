import pylab
from coords import coords
from mpl_toolkits.axes_grid.axislines import Subplot

params = {'backend': 'ps', 
          'axes.labelsize': 14, 
          'axes.titlesize': 16, 
          'text.fontsize': 14, 
          'legend.fontsize': 14, 
          'xtick.labelsize': 14, 
          'ytick.labelsize': 14, 
          'text.usetex': True} 
pylab.rcParams.update(params) 

settings = {'sensor_nodes': True,
            'sensor_ranges': True,
            'super_nodes': True,
            'routes': True,
            'route_costs': True}

def generate_graph(chromosome, nearest_supers, FIELD_WIDTH, FIELD_HEIGHT, 
                   graph_title, n):
    chromosome = [ int(i) for i in chromosome ]
    w = (FIELD_WIDTH)/4.0
    h = (FIELD_HEIGHT)/4.0
    fig = pylab.figure(figsize=(w+1,h))
    #fig = pylab.figure(figsize=(2.5,3))
    #ax = pylab.subplot(111)
    ax = Subplot(fig, 111)
    fig.add_subplot(ax)

    #ax.axis["right"].set_visible(False)
    #ax.axis["top"].set_visible(False)
    #ax.axis["bottom"].set_visible(False)
    #ax.axis["left"].set_visible(False)

    super_x = [ coords[i][0] for i in range(len(chromosome)) 
                if (chromosome[i] == 1) ]
    super_y = [ coords[i][1] for i in range(len(chromosome)) 
                if chromosome[i] == 1 ]
    sensor_x = [ coords[i][0] for i in range(len(chromosome)) 
                 if chromosome[i] == 0 ]
    sensor_y = [ coords[i][1] for i in range(len(chromosome)) 
                 if chromosome[i] == 0 ]
    target_x = 0
    target_y = 0
    #pylab.grid(True)

    for i, node in enumerate(chromosome):
        if node == 1:
            ax.plot([coords[i][0], 0], [coords[i][1], 0], '--',lw=.85, 
                    color='red')
        if not node and nearest_supers[i] >= 0:
            ax.plot([coords[i][0], 
                     coords[nearest_supers[i]][0]],
                    [coords[i][1], 
                     coords[nearest_supers[i]][1]],
                    '-', lw=.85, color='blue')

    ax.plot(sensor_x, sensor_y, 'go', label=r'sensor')
    ax.plot(super_x, super_y, 'bo', label=r'super')
    ax.plot(target_x, target_y, 'ro', label=r'target')
    #add_ranges(ax, chromosome)
    #draw_clusters(ax, chromosome, nearest_supers)
    pylab.xticks(pylab.arange(0, FIELD_WIDTH+1, 1), color='white')
    pylab.yticks(pylab.arange(0, FIELD_HEIGHT+1, 1), color='white')
    #ax.set_xticklabels([])
    #ax.set_yticklabels([])
    #pylab.title(graph_title)
    pylab.xlim((-1, FIELD_WIDTH+1))
    pylab.ylim((-1, FIELD_HEIGHT+1))
    ax.set_aspect(1)

    #legend(loc='right', bbox_to_anchor=(2,1))
    #box = ax.get_position()
    #ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    #ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    #box = ax.get_position()
    #ax.set_position([box.x0, box.y0 + box.height * 0.1,
    #                 box.width, box.height * 0.9])
    #ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
    #      fancybox=True, shadow=True, ncol=5,numpoints=1)

    #LEGEND
    #box = ax.get_position()
    #ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    #ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), numpoints=1)

    filename = "/home/milleraj/Desktop/genetic_graphs/chrom%d.pdf" % n
    print filename 
    pylab.savefig(filename)

def add_ranges(ax, chromosome, sensor=True):
    for i, xy in enumerate(coords):
        if sensor:
            if chromosome[i] == 0:
                ax.add_patch(pylab.Circle(xy, radius=3.0, alpha=0.15, 
                             fc='g', ec='none'))
        else:
            if chromosome[i] == 1:
                ax.add_patch(pylab.Circle(xy, radius=8.0, alpha=0.1, 
                             fc='b'))

def draw_clusters(ax, chromosome, nearest_supers):
    print nearest_supers
    supers = set(nearest_supers)
    print supers
    for super in supers:
        if super != -1:
            print coords[super]
    coordinates = []
    for i, node in enumerate(chromosome):
        if nearest_supers[i] == 49:
            coordinates.append(coords[i])

    print coordinates
    #[(10, 8), (10, 10), (13, 9), (13, 10), (12, 10), (10, 8), (7, 8), (11, 14), (15, 8)]
    


    #for i, xy in enumerate(coords):
