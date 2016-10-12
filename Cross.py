import random
import numpy as np

def Cross(chromosome1,chromosome2):
    random.seed()
    nGenes=len(chromosome1)
    newChromosomePair=np.zeros((2,nGenes))
    crossoverPoint=random.randint(0,nGenes-1)
    for j in range(nGenes):
        if j<crossoverPoint:
            newChromosomePair[0,j]=chromosome1[j]
            newChromosomePair[1,j]=chromosome2[j]
        else:
            newChromosomePair[0,j]=chromosome2[j]
            newChromosomePair[1,j]=chromosome1[j]
    return newChromosomePair

if __name__ == '__main__':
    chromosomeSize=20
    variableRange=2.0
    chromosome1=np.zeros(chromosomeSize)
    chromosome2=np.zeros(chromosomeSize)
    for j in range(chromosomeSize):
            s1=random.random()
            s2=random.random()
            if (s1<0.5):
                chromosome1[j]=0
            else:
                chromosome1[j]=1
            if (s2<0.5):
                chromosome2[j]=0
            else:
                chromosome2[j]=1
    crossedChromos=Cross(chromosome1,chromosome2)
    print('chromosome1: '+str(chromosome1)+'\n')
    print('crossed chromosome1: '+str(crossedChromos[0])+'\n')
    print('chromosome2: '+str(chromosome2)+'\n')
    print('crossed chromosome2: '+str(crossedChromos[1])+'\n')
