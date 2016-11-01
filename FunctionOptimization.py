import numpy as np
import random
from InitializePopulation import InitializePopulation
from DecodeChromosome import DotaDecode
from EvaluateIndividual import DotaEvaluate, LoadAdvantages
from TournamentSelect import TournamentSelect
from Cross import Cross
from Mutate import Mutate
import os
import time

if __name__ == '__main__':
    FunctionOptimization(99)

def FunctionOptimization(run):
    # seed=os.urandom(8)
    seed=run
    random.seed(seed)
    populationSize=100;
    numberOfVariables=30;
    numberOfGenes=10*numberOfVariables;
    crossoverProbability=0.8;
    mutationProbability=0.033;
    tournamentSelectionParameter=0.9;
    tournamentSize=5;
    numberOfGenerations=1000;
    variableRange=1.0;
    fitness=np.zeros(populationSize)
    numberOfRuns=1
    numberOfCopies=1
    results=np.zeros((numberOfRuns,numberOfVariables))
    bestFitnesses=np.zeros(numberOfRuns)
    mat=LoadAdvantages(numberOfVariables)

    for iRun in range(numberOfRuns):
        # print("run "+str(iRun))
        population=InitializePopulation(populationSize,numberOfGenes)
        print(population)
        xBest=np.zeros(numberOfVariables)
        bestIndividualIndex=0

        for iGeneration in range(numberOfGenerations):
            fitness=np.zeros(populationSize)
            print("generation "+str(iGeneration)+" "+str(time.time())+"\n")
            maximumFitness=0.0
            decodedPopulation=np.zeros((populationSize,numberOfVariables))
            for i in range(populationSize):
                chromosome=population[i,:]
                x=DotaDecode(chromosome,numberOfVariables,variableRange)
                decodedPopulation[i,:]=x[:]
            # print(decodedPopulation)
            for i in range(populationSize):
                y=[]
                for j in range(populationSize):
                    if i==j:
                        continue

                    x[:]=decodedPopulation[i,:]
                    y[:]=decodedPopulation[j,:]
                    fitness[i]=fitness[i]+DotaEvaluate(x,y,numberOfVariables,mat)[0]  ### NEED TO THINK ON HOW TO IMPLEMENT EVALUATION: TOURNAMENT?
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

    filename="tst_"+str(run)+".log"
    fp=open(filename,"w")
    for i in range(populationSize):
        chromosome=population[i,:]
        x=DotaDecode(chromosome,numberOfVariables,variableRange)
        fp.write(str(x)+"\n")
    fp.write(str(fitness)+"\n")
    fp.close()
