import numpy as np
import random

def TournamentSelect(fitness,tournamentSelectionParameter,tournamentSize):
    random.seed()
    populationSize=len(fitness)
    iTmp=np.zeros(tournamentSize)
    localFitness=np.zeros(tournamentSize)
    for i in range(tournamentSize):
        iTmp[i]=random.randint(0,populationSize-1)
        localFitness[i]=fitness[int(iTmp[i])]

    r=random.random()
    while r>tournamentSelectionParameter:
        maxVal=max(localFitness)
        indexMax=np.argmax(localFitness)
        if np.count_nonzero(iTmp)>1:
            iTmp[indexMax]=0
            localFitness[indexMax]=0
        else:
            break
        r=random.random()
    maxVal=max(localFitness)
    indexMax=np.argmax(localFitness)
    iSelected=iTmp[indexMax]
    return iSelected




if __name__ == '__main__':

    numberChromosomes=10
    fitness=np.random.random(numberChromosomes)
    tournamentSelectionParameter=0.75;
    tournamentSize=4;
    iterations=1000;
    selected=np.zeros(iterations)


    for i in range(iterations):
        selected[i]=TournamentSelect(fitness,tournamentSelectionParameter,tournamentSize)
    [probab,bins]=np.histogram(selected,bins=numberChromosomes,density=True)
    print(probab)
    for i in range(numberChromosomes):
        print("chromosome "+str(i)+" fitness "+str(fitness[i])+" chosen "+str(probab[i])+" of times")
