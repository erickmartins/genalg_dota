def InsertBestIndividual(population,bestChromosome,numberOfCopies):
    tempPopulation=population
    # print(tempPopulation[bestIndividual])

    for i in range(numberOfCopies):
        tempPopulation[i,:]=bestChromosome[:]
    # print (tempPopulation[0])
    return tempPopulation


if __name__=="__main__":
    import numpy as np
    numberOfVariables=10
    pop=np.random.choice([0,1],size=(numberOfVariables,numberOfVariables))
    bestIndividual=2
    numberOfCopies=1
    print(pop)
    pop=InsertBestIndividual(pop,bestIndividual,numberOfCopies)
    print(pop)
