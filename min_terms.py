import math

expList = list()
termsMap = {}

def createExpList(target, exp):
    global expList
    expList = list()
    candidate = 1
    currNum = 2
    while(candidate <= target):

        expList.append(int(candidate))

        candidate = math.pow(currNum, exp)

        currNum = currNum + 1

def genChildren(target):
    childList = []
    i = 0

    for i in range(0,len(expList)):
        if (expList[i] <= target[0]):
            childList.append((target[0]-expList[i], target[1] + 1))

    return childList

def min_terms(target, exp):

    createExpList(target, exp)

    print(expList)

    global termsMap
    termsMap = {}

    termsMap[target] = 0
    newTermsMap = {}

    while(0 not in termsMap):

        for key,value in termsMap.items():

            children = genChildren((key,value))
            
            for (k,v) in children:

                newTermsMap[k] = v

        termsMap = newTermsMap.copy()

    return termsMap[0]


print(min_terms(9,3))


