import numpy as np
import random

def Mutate(chromosome,mutationProbability):
    random.seed()
    nGenes=len(chromosome)
    mutatedChromosome=chromosome[:]
    for j in range(nGenes):
        r=random.random()
        if (r<mutationProbability):
            mutatedChromosome[j]=1-chromosome[j]

    return mutatedChromosome



if __name__ == '__main__':

    numberOfGenes=10;
    mutationProbability=0.1;
    chromosome=np.random.choice([0,1],size=(numberOfGenes))
    print("pre-mutation chromosome: "+str(chromosome))
    mutatedChromosome=Mutate(chromosome,mutationProbability)
    print("post-mutation chromosome: "+str(mutatedChromosome))
