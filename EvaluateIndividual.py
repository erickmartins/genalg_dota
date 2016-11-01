import numpy as np
import random
from bisect import bisect

def weighted_choice(list1,prob):
    total = 0
    cum_weights = []
    for w in prob:
        total += w
        cum_weights.append(total)
    x = random.random() * total
    i = bisect(cum_weights, x)
    return list1[i]

def EvaluateIndividual(x):
    random.seed()
    fitness=sum(x)
    return fitness

def LoadAdvantages(numberOfVariables):
    mat=np.zeros((numberOfVariables,numberOfVariables))
    fp=open("advantages_30.csv","r")

    for i in range(numberOfVariables):
        string=fp.readline()
        # print(string)
        lst=string.split(",")
        # print(lst)
        mat[i,:]=[float(j) for j in lst]
    fp.close()
    return mat

def DotaEvaluate(x,y,numberOfVariables,mat):
    # random.seed()

    # print(mat)
    pick1=np.zeros(5)
    pick2=np.zeros(5)
    list1=list(range(len(x)))
    list2=list(range(len(x)))
    for i in range(5):
        # pick1[i]=np.random.choice(list1,p=x)
        pick1[i]=weighted_choice(list1,x)
        x[int(pick1[i])]=0
        y[int(pick1[i])]=0
        y=y/sum(y)
        # pick2[i]=np.random.choice(list2,p=y)
        pick2[i]=weighted_choice(list2,y)
        x[int(pick2[i])]=0
        y[int(pick2[i])]=0
        x=x/sum(x)
    # print(pick1,pick2)
    fitness=np.zeros(2)
    for j in pick1:
        fitness[0]=fitness[0]+sum([mat[int(j),int(i)] for i in pick2])
    for j in pick2:
        fitness[1]=fitness[1]+sum([mat[int(j),int(i)] for i in pick1])

    # fp.close()
    # print(fitness)
    return fitness

if __name__ == '__main__':
    from DecodeChromosome import DotaDecode
    print("teste: ")
    numberOfVariables=30
    x=np.random.choice([0,1],size=numberOfVariables*10)
    xdec=DotaDecode(x,numberOfVariables,0.5)
    y=np.random.choice([0,1],size=numberOfVariables*10)
    ydec=DotaDecode(y,numberOfVariables,0.5)
    print(xdec,ydec)
    # print(DotaEvaluate(xdec,ydec,numberOfVariables))
    chosen=weighted_choice(range(numberOfVariables),xdec)
    print(chosen)
