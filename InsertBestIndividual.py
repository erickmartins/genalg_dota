import numpy as np
import random
from DecodeChromosome import DecodeChromosome

def InsertBestIndividual(population, bestIndividual,numberOfCopies):
    tempPopulation=population[:]
    for i in range(numberOfCopies):
        tempPopulation[i,:]=population[bestIndividual,:]
    return tempPopulation




if __name__ == '__main__':

    populationSize=50
    numberOfGenes=20
    variableRange=2.0
    numberOfCopies=4
    population=np.random.choice([0,1],size=(populationSize,numberOfGenes))
    bestIndividual=random.randint(0,populationSize-1)
    bestChromosome=population[bestIndividual,:]
    print(DecodeChromosome(bestChromosome,4,variableRange))
    tempPopulation=InsertBestIndividual(population,bestIndividual,numberOfCopies)
    for i in range(numberOfCopies+1):
        print(DecodeChromosome(tempPopulation[i,:],4,variableRange))
