import numpy as np
import random
from InitializePopulation import InitializePopulation
from DecodeChromosome import DotaDecode
<<<<<<< HEAD
from EvaluateIndividual import DotaEvaluate, LoadAdvantages, randDotaEvaluate
=======
from EvaluateIndividual import DotaEvaluate
>>>>>>> parent of 5732fa1... efficiencies gained on evaluation, mainly
from TournamentSelect import TournamentSelect
from Cross import Cross
from Mutate import Mutate
from InsertBestIndividual import InsertBestIndividual
import os



def FunctionOptimization(run):
    # seed=os.urandom(8)
    seed=run
    random.seed(seed)
    numberOfCopies=1
    populationSize=100;
    numberOfVariables=30;
    numberOfGenes=10*numberOfVariables;
    crossoverProbability=0.5;
    mutationProbability=0.033;
    tournamentSelectionParameter=0.8;
    tournamentSize=5;
<<<<<<< HEAD
    numberOfGenerations=10000;
=======
    numberOfGenerations=1;
>>>>>>> parent of 5732fa1... efficiencies gained on evaluation, mainly
    variableRange=1.0;
    fitness=np.zeros(populationSize)
    numberOfRuns=1
    numberOfCopies=1
    results=np.zeros((numberOfRuns,numberOfVariables))
    bestFitnesses=np.zeros(numberOfRuns)
<<<<<<< HEAD
    mat=LoadAdvantages(numberOfVariables)
    bestChromosome=np.zeros(numberOfGenes)
=======

>>>>>>> parent of 5732fa1... efficiencies gained on evaluation, mainly
    for iRun in range(numberOfRuns):
        # print("run "+str(iRun))
        population=InitializePopulation(populationSize,numberOfGenes)
        print(population)
        xBest=np.zeros(numberOfVariables)
        bestIndividualIndex=0
        maximumFitness=0
        for iGeneration in range(numberOfGenerations):
            fitness=np.zeros(populationSize)
<<<<<<< HEAD

=======
            print("generation "+str(iGeneration))
>>>>>>> parent of 5732fa1... efficiencies gained on evaluation, mainly
            maximumFitness=0.0
            decodedPopulation=np.zeros((populationSize,numberOfVariables))
            for i in range(populationSize):
                chromosome=population[i,:]
                x=DotaDecode(chromosome,numberOfVariables,variableRange)
                decodedPopulation[i,:]=x[:]
            # print(decodedPopulation)
            for i in range(populationSize):
                y=[]
<<<<<<< HEAD
                # for j in range(populationSize):
                #     if i==j:
                #         continue
                #
                x[:]=decodedPopulation[i,:]
                #     y[:]=decodedPopulation[j,:]
                fitness[i]=randDotaEvaluate(x,numberOfVariables,mat)  ### NEED TO THINK ON HOW TO IMPLEMENT EVALUATION: TOURNAMENT?
=======
                for j in range(populationSize):
                    if i==j:
                        continue

                    x[:]=decodedPopulation[i,:]
                    y[:]=decodedPopulation[j,:]
                    fitness[i]=fitness[i]+DotaEvaluate(x,y,numberOfVariables)[0]  ### NEED TO THINK ON HOW TO IMPLEMENT EVALUATION: TOURNAMENT?
>>>>>>> parent of 5732fa1... efficiencies gained on evaluation, mainly
                if fitness[i]>maximumFitness:
                    maximumFitness=fitness[i]
                    bestIndividualIndex=i
                    bestChromosome[:]=population[i,:]
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
            # print(population[0,:])
            # print(population[bestIndividualIndex,:])
            population[:]=InsertBestIndividual(population,bestChromosome,numberOfCopies)
            # print(population[0,:])
            print("generation "+str(iGeneration)+" "+str(time.time())+"best fitness: "+str(maximumFitness)+" best individual: "+str(bestIndividualIndex)+"\n")
            # print(fitness)
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




if __name__ == '__main__':
    FunctionOptimization(99)
