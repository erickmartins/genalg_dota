import multiprocessing
import time
from FunctionOptimization import FunctionOptimization
import random
import os

def TestFunc(num):
    seed=os.urandom(8)
    random.seed(seed)
    tot=100
    res=1
    for i in range(tot):
        res+=random.random()
    print(res,num)
    t2=time.time()
    print(t2)
    # time.sleep(2)
    return res




def SpawnMultiple(runs,func):
    jobs=[]
    for i in range(runs):
        p=multiprocessing.Process(target=func,args=(i,))
        jobs.append(p)
        p.start()

    # for i in jobs:
    #     i.join()


def seqrun(runs,func):
    for i in range(runs):
        func(99)
    t2=time.time()
    print(t2)

if __name__ == '__main__':
    runs=4
    # func=TestFunc
    func=FunctionOptimization
    # t1=time.time()
    # print(t1)
    SpawnMultiple(runs,func)
    # seqrun(runs,func)
    # t2=time.time()-t1
    # print(t2)
