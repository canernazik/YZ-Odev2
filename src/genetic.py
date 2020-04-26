import numpy as np
import copy
from PIL import Image
import scipy.misc

class child:

    def __init__(self,fit,path):
        self.fit=fit
        self.path = path
#pop = yaratacağımız popülasyonun sayısı
def createPopulation(population,pop):
    for x in range(pop):
        population.append(child(0,np.random.randint(1,5,40)))

    return population


def createRoulette(population,roulette,pop):
    for x in range(pop):
        for y in range(10): #range'nin içi population[x].fit olacak fit değeri en başta 0 olduğu için şimdilik hata veriyor findFit fonksiyonunu kullakdıktan sonra çalışır
            roulette.append(x)

    return roulette

#öncesinde fite göre sort at
def nextGen(population,roulette,pop):  #yeni jenerasyonu bulma fonksiyonu
    newGen = []
    roulette = createRoulette(population,roulette,pop)
    for x in range(int(pop/2)):
        newGen.append(population[x])
    for x in range(int(pop/4)):

        random1 = roulette[np.random.randint(0,len(roulette))]
        random2 = roulette[np.random.randint(0,len(roulette))]
        randomGen = np.random.randint(0,40)
        newPerson = crossover(random1,random2,randomGen,population)
        newGen.append(newPerson)
        newPerson = crossover(random2,random1,randomGen,population)
        newGen.append(newPerson)
    for x in range(3):
        mut = np.random.randint(50,100)
        mutation(newGen[mut])
    return newGen

def crossover(random1,random2,randomGen,population):        #crossover fonksiyonu
    path = []
    for x in range(randomGen):
        path.append(population[random1].path[x])
    for x in range(randomGen,40):
        path.append(population[random2].path[x])
    newPerson = child(0,path)
    return newPerson

def mutation(person):       #mutasyon fonksiyonu
    random1 = np.random.randint(0,40)
    random2 = np.random.randint(0, 40)
    person.path[random1], person.path[random2] = person.path[random2], person.path[random1]

def findFit(person,maze):       #fit değerini bulma fonksiyonu (maze olmadığı için kontrol edemedim doğruluğu
    fit=0
    i=1
    j=1
    k=0
    while (maze[i][j] != 1 and (i!=len(maze)-2 or j!=len(maze)-2) and k < 40):
        maze[i][j] = 1 ## Daha onceden  geldigi yere tekrar gelmesin diye sanki burada engel varmıs gibi gosteriliyor.
        if (person.path[k] == 1):
            j=j-1
        elif (person.path[k] == 2):
            i=i-1
        elif (person.path[k] == 3):
            j=j+1
        elif (person.path[k] == 4):
            i=i+1
        fit = fit+1
        k=k+1
    if (i==len(maze)-2 and j==len(maze)-2):
        fit=fit+100000

    return fit

def printBest(person,maze):
    img = np.zeros((len(maze), len(maze), 3), dtype=np.uint8)
    i = 1
    j = 1
    for x in range(person.fit-100000):
        maze[i][j] = 2
        if (person.path[x] == 1):
            j=j-1
        elif (person.path[x] == 2):
            i=i-1
        elif (person.path[x] == 3):
            j=j+1
        elif (person.path[x] == 4):
            i=i+1
    for x in range(len(maze)-1):
        for y in range(len(maze)-1):
            if (maze[x][y]==0):
                img[x][y]=[255,255,255]

            elif (maze[x][y]==1):
                img[x][y]=[0,0,0]
            elif (maze[x][y]==2):
                img[x][y] = [100, 100, 100]
    return  img


# Jenerasyon sayısı önemli yani kaç tane jenerasyon yaratılacak yani döngü sayısı bir nevi
population = []
roulette = []
createPopulation(population,100)
copymaze = []
maze = [[1,1,1,1,1,1,1,1],
        [1,0,0,1,1,1,1,1],
        [1,0,1,1,0,0,0,1],
        [1,0,1,1,0,0,0,1],
        [1,0,0,0,0,0,0,1],
        [1,1,1,0,0,0,0,1],
        [1,1,1,1,1,1,0,1],
        [1,1,1,1,1,1,1,1]]
while (population[0].fit < 100000):
    for x in (population):
        copymaze = copy.deepcopy(maze)
        x.fit=findFit(x,copymaze)
    population.sort(key=lambda x: x.fit,reverse=True)
    population=nextGen(population,roulette,100)
    print(population[0].fit)

print(population[0].path)
copymaze = copy.deepcopy(maze)
data = printBest(population[0],copymaze)
img = Image.fromarray(data, 'RGB')
img.show()




