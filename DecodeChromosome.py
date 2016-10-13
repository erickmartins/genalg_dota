import numpy as np
import random
from math import *

def DecodeChromosome(chromosome, numberOfVariables, variableRange):
    nGenes=len(chromosome)
    genesPerVariable=round(nGenes/numberOfVariables)
    x=np.zeros(numberOfVariables)

    for i in range(numberOfVariables):
        for j in range(genesPerVariable):
            index=int(j+i*genesPerVariable)
            x[i]=x[i]+chromosome[index]*pow(2.,(-1.*(j+1.)))
        x[i]=-1.*variableRange+2.*variableRange*x[i]/(1-pow(2.,(-1.*genesPerVariable)))

    return x



def DotaDecode(chromosome,numberOfVariables,variableRange):
    x=DecodeChromosome(chromosome,numberOfVariables,variableRange)
    x=x+variableRange
    x=x/sum(x)
    return x




if __name__ == '__main__':
    random.seed()
    chromosomeSize = 100
    numberOfVariables = 10
    variableRange=0.5
    chromosome=np.zeros(chromosomeSize)
    for i in range(chromosomeSize):
        r=random.random()
        if (i+1)+4<0.5*chromosomeSize:
            chromosome[i]=0
        else:
            chromosome[i]=1
    decodedVariables=DotaDecode(chromosome,numberOfVariables,variableRange)
    for i in range(numberOfVariables):
        print("variable "+str(i)+": "+str(decodedVariables[i]))
    print("sum: "+str(sum(decodedVariables)))
