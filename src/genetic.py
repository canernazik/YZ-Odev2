import numpy as np

class child:

    def __init__(self,fit,path):
        self.fit=fit
        self.path = path
#pop = yaratacağımız popülasyonun sayısı
def createPopulation(population,pop):
    for x in range(pop):
        population.append(child(0,np.random.randint(1,5,40)))

    return population


population = []
createPopulation(population,100)
