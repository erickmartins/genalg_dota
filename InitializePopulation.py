import numpy as np
import random


def InitializePopulation(populationSize,numberOfGenes):
    random.seed()
    population=np.random.choice([0, 1],size=(populationSize,numberOfGenes))
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
