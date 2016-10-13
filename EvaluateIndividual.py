import numpy as np
import random


def EvaluateIndividual(x):
    random.seed()
    fitness=sum(x)
    return fitness


def DotaEvaluate(x,y,numberOfVariables):
    random.seed()
    mat=np.zeros((numberOfVariables,numberOfVariables))
    for i in range(numberOfVariables):  ### MAT NEEDS TO BE LOADED FROM ADVANTAGES MATRIX 
        for j in range(i):
            mat[i,j]=2.*random.random()-1.
            mat[j,i]=-1.*mat[i,j]
    print(mat)
    pick1=np.zeros(5)
    pick2=np.zeros(5)
    for i in range(5):
        pick1[i]=np.random.choice(range(len(x)),p=x)
        x[int(pick1[i])]=0
        y[int(pick1[i])]=0
        y=y/sum(y)
        pick2[i]=np.random.choice(range(len(y)),p=y)
        x[int(pick2[i])]=0
        y[int(pick2[i])]=0
        x=x/sum(x)
    print(pick1,pick2)
    fitness=np.zeros(2)
    for j in pick1:
        fitness[0]=fitness[0]+sum([mat[j,int(i)] for i in pick2])
    for j in pick2:
        fitness[1]=fitness[1]+sum([mat[j,int(i)] for i in pick1])


    print(fitness)
    return fitness

if __name__ == '__main__':
    from DecodeChromosome import DotaDecode
    print("teste: ")
    numberOfVariables=10
    x=np.random.choice([0,1],size=numberOfVariables*10)
    xdec=DotaDecode(x,numberOfVariables,0.5)
    y=np.random.choice([0,1],size=numberOfVariables*10)
    ydec=DotaDecode(y,numberOfVariables,0.5)
    print(DotaEvaluate(xdec,ydec,numberOfVariables))
