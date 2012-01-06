from pylab import *

def generate_graph(chromosome, nearest_supers, FIELD_WIDTH, FIELD_HEIGHT, coords, graph_title):
    chromosome = [ int(i) for i in chromosome ]
    ax = subplot(111)
    super_x = [ coords[i][0] for i in range(len(chromosome)) if (chromosome[i] == 1) ]
    super_y = [ coords[i][1] for i in range(len(chromosome)) if chromosome[i] == 1 ]
    sensor_x = [ coords[i][0] for i in range(len(chromosome)) if chromosome[i] == 0 ]
    sensor_y = [ coords[i][1] for i in range(len(chromosome)) if chromosome[i] == 0 ]
    target_x = 0
    target_y = 0
    grid(True)

    for i, node in enumerate(chromosome):
        if node == 1:
            ax.plot([coords[i][0], 0], [coords[i][1], 0], '-', color='red')
        if not node and nearest_supers[i] >= 0:
            ax.plot([coords[i][0], 
                     coords[nearest_supers[i]][0]],
                    [coords[i][1], 
                     coords[nearest_supers[i]][1]],
                    '-', color='blue')

    ax.plot(sensor_x, sensor_y, 'go', label=r'$sensor$')
    ax.plot(super_x, super_y, 'bo', label=r'$super$')
    ax.plot(target_x, target_y, 'ro', label=r'$target$')
    xticks(arange(0, FIELD_WIDTH+1, 1), ['$%d$' % i for i in range(0, FIELD_WIDTH+1)], fontsize=10)
    yticks(arange(0, FIELD_HEIGHT+1, 1), ['$%d$' % i for i in range(0, FIELD_HEIGHT+1)], fontsize=10)
    title(graph_title, fontsize=16)
    xlim((-1, FIELD_WIDTH+1))
    ylim((-1, FIELD_HEIGHT+1))
    #legend(loc='right', bbox_to_anchor=(2,1))
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    ax.legend(numpoints=1, loc='center left', bbox_to_anchor=(1, 0.5))

    filename = "./ga-plot.pdf"
    print filename
    savefig(filename)
