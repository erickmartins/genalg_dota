import numpy as np
import random
from InitializePopulation import InitializePopulation
from DecodeChromosome import DotaDecode
from EvaluateIndividual import EvaluateIndividual
from TournamentSelect import TournamentSelect
from Cross import Cross
from Mutate import Mutate

if __name__ == '__main__':

    populationSize=100;
    numberOfGenes=60;
    numberOfVariables=2;
    crossoverProbability=0.8;
    mutationProbability=0.033;
    tournamentSelectionParameter=0.9;
    tournamentSize=5;
    numberOfGenerations=100;
    variableRange=5.0;
    fitness=np.zeros(populationSize)
    numberOfRuns=2
    numberOfCopies=1
    results=np.zeros((numberOfRuns,numberOfVariables))
    bestFitnesses=np.zeros(numberOfRuns)

    for iRun in range(numberOfRuns):
        print("run "+str(iRun))
        population=InitializePopulation(populationSize,numberOfGenes)
        xBest=np.zeros(numberOfVariables)
        bestIndividualIndex=0

        for iGeneration in range(numberOfGenerations):
            maximumFitness=0.0
            decodedPopulation=np.zeros((populationSize,numberOfVariables))
            for i in range(populationSize):
                chromosome=population[i,:]
                x=DotaDecode(chromosome,numberOfVariables,variableRange)
                decodedPopulation[i,:]=x[:]
                fitness[i]=EvaluateIndividual(x)  ### NEED TO THINK ON HOW TO IMPLEMENT EVALUATION: TOURNAMENT?
                if fitness[i]>maximumFitness:
                    maximumFitness=fitness[i]
                    bestIndividualIndex=i
                    xBest=x

            tempPopulation=population[:]

            for i in range(0,populationSize,2):
                i1=TournamentSelect(fitness,tournamentSelectionParameter,tournamentSize)
                i2=TournamentSelect(fitness,tournamentSelectionParameter,tournamentSize)
                chromosome1=population[int(i1),:]
                chromosome2=population[int(i2),:]

                r=random.random()
                if r<crossoverProbability:
                    newChromosomePair=Cross(chromosome1,chromosome2)
                    tempPopulation[i,:]=newChromosomePair[0,:]
                    tempPopulation[i+1,:]=newChromosomePair[1,:]
                else:
                    tempPopulation[i,:]=chromosome1[:]
                    tempPopulation[i+1,:]=chromosome2[:]

            for i in range(populationSize):
                originalChromosome=population[i,:]
                mutatedChromosome=Mutate(originalChromosome,mutationProbability)
                tempPopulation[i,:]=mutatedChromosome[:]
            population[:]=tempPopulation[:]
        results[iRun,:]=xBest
        bestFitnesses[iRun]=maximumFitness


    print(results)
    print(bestFitnesses)
