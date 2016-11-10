import numpy as np
import matplotlib.pyplot as plt
import sys


if __name__=="__main__":
    filename=sys.argv[1]
    fp=open(filename,'r')
    line=fp.readline()
    numberOfVariables=30
    populationSize=10
    results=np.zeros([populationSize,numberOfVariables])
    templist=[]
    linecount=0
    while (line) and linecount<populationSize:
        # print(line)
        sep=line.split()
        if sep[0]=="[":
            templist=[float(i) for i in sep[1:]]
            # print("line start")
            # print(templist)
        elif sep[0].startswith("[") and len(sep[0])>2:
            templist.append(float(sep[0][1:]))
            templist=[float(i) for i in sep[1:]]
            # print("line start")
            # print(templist)
        elif sep[-1].endswith("]") and len(sep[-1])>2:
            templist+=[float(i)for i in sep[:-1]]
            templist.append(float(sep[-1][:-1]))
            results[linecount,:]=templist
            # print(results)
            linecount+=1
        elif sep[-1].endswith("]")and len(sep[-1])<=2:
            templist+=[float(i)for i in sep[:-1]]
            results[linecount,:]=templist
            # print(results)
            linecount+=1
        else:
            templist+=[float(i)for i in sep[:]]
            # print(templist)
        line=fp.readline()
    test=np.mean(results,axis=0)
    plt.bar(range(len(test)),test)
    plt.show(block=True)
    # arr=np.array([float(i) for i in string.split()])
#
# plt.bar(range(len(arr)),arr)
# plt.show(block=True)
