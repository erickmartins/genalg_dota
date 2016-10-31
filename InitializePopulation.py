import numpy as np
import random
import os


def InitializePopulation(populationSize,numberOfGenes):
    seed=os.urandom(8)
    random.seed(seed)
    newseed=random.randint(0,1000000)
    # print(newseed)
    np.random.seed(newseed)
    population=np.random.choice([0, 1],size=(populationSize,numberOfGenes))
    # print (population)
    return population




if __name__ == '__main__':

    populationSize = 50
    numberOfGenes = 20
    population=InitializePopulation(populationSize,numberOfGenes)

    print("number of lines: "+str(populationSize))
    print("number of columns "+str(numberOfGenes))
    totalOnes=np.sum(population)
    # print(totalOnes)
    proportion=totalOnes/(populationSize*numberOfGenes)

    print("proportion of ones: "+str(proportion))
