import numpy as np
import random


def EvaluateIndividual(x):
    random.seed()
    fitness=sum(x)
    return fitness




if __name__ == '__main__':

    print("teste: "+str(EvaluateIndividual(10)))
