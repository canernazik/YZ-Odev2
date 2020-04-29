import numpy as np
import copy
import matplotlib.pyplot as plt
from matplotlib import colors
from maze import Maze


class child:
    def __init__(self,fit,path):
        self.fit=fit
        self.path = path


chromosome_length = 100
        
def createPopulation(population, size):
    for x in range(size):
        population.append(child(0,np.random.randint(1,5,chromosome_length)))

    return population


def createRoulette(population,roulette,pop):
    for x in range(pop):
        for y in range(population[x].fit):
            roulette.append(x)

    return roulette

def nextGen(population,roulette,population_size):
    newGen = []
    roulette = createRoulette(population,roulette,population_size)
    for x in range(int(population_size/2)):
        newGen.append(population[x])
    for x in range(int(population_size/4)):

        parent_1 = roulette[np.random.randint(0,len(roulette))]
        parent_2 = roulette[np.random.randint(0,len(roulette))]
        
        # Duvara carpana kadar olan gen alındı
        randomGen = population[parent_1].fit
        
        if (randomGen > 100000):
            randomGen=randomGen-100000
        
        # child - 1
        newPerson = crossover(parent_1,parent_2,randomGen,population)
        newGen.append(newPerson)
        
        #Child - 2
        newPerson = crossover(parent_2,parent_1,randomGen,population)
        newGen.append(newPerson)
    
    for x in range(int(population_size/10)):
        mut = np.random.randint(0,population_size)
        mutation(newGen[mut])
                                
    return newGen


def crossover(parent_1,parent_2,randomGen,population):
    path = []
    
    for x in range(randomGen):
        path.append(population[parent_1].path[x])
    
    for x in range(randomGen,chromosome_length):
        path.append(population[parent_2].path[x])
    
    newPerson = child(0,path)
    
    return newPerson

def mutation(person):
    gen_position_1 = np.random.randint(0, chromosome_length)
    gen_position_2 = np.random.randint(0, chromosome_length)
    person.path[gen_position_1], person.path[gen_position_2] = person.path[gen_position_2], person.path[gen_position_1]


""" alternatif fit fonksiyonu
def findFit(person,maze):
    fit=0
    i=1
    j=1
    k=0
    while (maze[i][j] != 1 and (i!=len(maze)-2 or j!=len(maze)-2) and k < 100):
        maze[i][j] = 1 ## Daha onceden  geldigi yere tekrar gelmesin diye sanki burada engel varmıs gibi gosteriliyor.
        if (person.path[k] == 1):
            j=j-1
        elif (person.path[k] == 2):
            i=i-1
        elif (person.path[k] == 3):
            j=j+1
        elif (person.path[k] == 4):
            i=i+1
        fit = i+j
        k=k+1
    if (i==len(maze)-2 and j==len(maze)-2):
        fit=fit+100000

    return fit """

def findFit(person,maze):
    fit=0
    i=1
    j=1
    k=0
    while (maze[i][j] != 1 and (i!=len(maze)-2 or j!=len(maze)-2) and k < chromosome_length):
        maze[i][j] = 1 ## Daha onceden  geldigi yere tekrar gelmesin diye sanki burada engel varmıs gibi gosteriliyor.
        if (person.path[k] == 1):
            j=j-1
        elif (person.path[k] == 2):
            i=i-1
        elif (person.path[k] == 3):
            j=j+1
        elif (person.path[k] == 4):
            i=i+1
        k=k+1
    fit = i+j
    if (i==len(maze)-2 and j==len(maze)-2):
        fit=fit+100000

    return fit


population_size=200
population = []
roulette = []
createPopulation(population,population_size)
copymaze = []
counter = 1

maze = Maze(20, 20, 10).get_matrix()

while (population[0].fit < 100000):
    for x in (population):
        copymaze = copy.deepcopy(maze)
        x.fit=findFit(x,copymaze)
    population.sort(key=lambda x: x.fit, reverse=True)
    population=nextGen(population,roulette,population_size)
    
    
    data = copy.deepcopy(maze)
    chromosome = population[0].path
    fit = population[0].fit
    
    """ Video çekerken kullanıldı
    k = 0
    i,j = 1,1
    
    if fit > 100000:
        fit = fit - 100000
    
    while fit != 0 and ((i < len(data) and i > -1) and (len(data) > j and j > -1)) and data[i][j] != 1:
        if chromosome[k] == 1:
            j = j - 1
        elif chromosome[k] == 2:
            i = i - 1
        elif chromosome[k] == 3:
            j = j + 1
        else:
            i = i + 1
    
        data[i][j] = 15
        k = k + 1
        fit = fit - 1
    
    data[1][1] = 8
    data[len(data)-2][len(data[0])-2] = 8
    
    
    
    cmap = colors.ListedColormap(['white', 'red', 'green', 'orange'])
    bounds = [0,0.9, 5, 10, 20]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    
    fig, ax = plt.subplots(figsize=(8,9))
    ax.imshow(data, cmap=cmap, norm=norm)
    
    # draw gridlines
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
    ax.set_xticks(np.arange(-.5, len(maze), 1));
    ax.set_yticks(np.arange(-.5, len(maze), 1));

    plt.setp(ax.get_xticklabels(), visible=False)
    plt.setp(ax.get_yticklabels(), visible=False)
    
    plt.text(-1,-1, "Generation: " + str(counter), fontsize=12, weight="bold")
    
    path = "4/gen_" + str(counter) + ".png"
    
    fig.savefig(path)
    """
    
    counter = counter +1
    print(population[0].fit)
    

print(population[0].path)
print(population[0].fit-100000)
print(counter)
copymaze = copy.deepcopy(maze)

data = copy.deepcopy(maze)
data[1][1] = 8
data[len(data)-2][len(data[0])-2] = 8

chromosome = population[0].path

k = 0
i,j = 1,1

while (i != len(data)-2 or j != len(data[0])-2 ) and (k < len(chromosome)):
    if chromosome[k] == 1:
        j = j - 1
    elif chromosome[k] == 2:
        i = i - 1
    elif chromosome[k] == 3:
        j = j + 1
    else:
        i = i + 1

    data[i][j] = 15
    k = k + 1

data[1][1] = 8
data[len(data)-2][len(data[0])-2] = 8

# 0 - 0.9 değerleri arası beyaz, 0.9-5 arası kırmızı, 5-10 yesil, 10-20 yesil
# olarak matriste gosterilir
cmap = colors.ListedColormap(['white', 'red', 'green', 'orange'])
bounds = [0,0.9, 5, 10, 20]
norm = colors.BoundaryNorm(bounds, cmap.N)

fig, ax = plt.subplots(figsize=(8,9))
ax.imshow(data, cmap=cmap, norm=norm)

# kareler arasında siyah cizgiler cizilir
ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
ax.set_xticks(np.arange(-.5, len(maze), 1));
ax.set_yticks(np.arange(-.5, len(maze), 1));

plt.setp(ax.get_xticklabels(), visible=False)
plt.setp(ax.get_yticklabels(), visible=False)

plt.show()
