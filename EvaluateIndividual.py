import numpy as np
import random


def EvaluateIndividual(x):
    random.seed()
    fitness=sum(x)
    return fitness


def DotaEvaluate(x,y,numberOfVariables):
    random.seed()
    mat=np.zeros((numberOfVariables,numberOfVariables))
    fp=open("advantages_30.csv","r")

    for i in range(numberOfVariables):
        string=fp.readline()
        # print(string)
        lst=string.split(",")
        # print(lst)
        mat[i,:]=[float(j) for j in lst]
<<<<<<< HEAD
    fp.close()
    return mat

def randDotaEvaluate(x,numberOfVariables,mat):
    vec=np.array([1./numberOfVariables]*numberOfVariables)
    # print(vec)
    prod1=np.dot(x,mat)
    prod2=np.dot(prod1,vec)
    # print(x,prod2)
    return prod2


def DotaEvaluate(x,y,numberOfVariables,mat):
    # random.seed()

=======
>>>>>>> parent of 5732fa1... efficiencies gained on evaluation, mainly
    # print(mat)
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
    # print(pick1,pick2)
    fitness=np.zeros(2)
    for j in pick1:
        fitness[0]=fitness[0]+sum([mat[int(j),int(i)] for i in pick2])
    for j in pick2:
        fitness[1]=fitness[1]+sum([mat[int(j),int(i)] for i in pick1])

    fp.close()
    # print(fitness)
    return fitness

if __name__ == '__main__':
    from DecodeChromosome import DotaDecode
    # print("teste: ")
    numberOfVariables=30
    x=np.random.choice([0,1],size=numberOfVariables*10)
    xdec=DotaDecode(x,numberOfVariables,0.5)
<<<<<<< HEAD
    mat=LoadAdvantages(numberOfVariables)
    # y=np.random.choice([0,1],size=numberOfVariables*10)
    # ydec=DotaDecode(y,numberOfVariables,0.5)
    # print(xdec,ydec)
    # # print(DotaEvaluate(xdec,ydec,numberOfVariables))
    # chosen=weighted_choice(range(numberOfVariables),xdec)
    # print(chosen)

    fit=randDotaEvaluate(xdec,numberOfVariables,mat)
    print(fit)
=======
    y=np.random.choice([0,1],size=numberOfVariables*10)
    ydec=DotaDecode(y,numberOfVariables,0.5)
    print(xdec,ydec)
    print(DotaEvaluate(xdec,ydec,numberOfVariables))
>>>>>>> parent of 5732fa1... efficiencies gained on evaluation, mainly
