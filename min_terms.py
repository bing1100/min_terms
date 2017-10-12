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

def dpStep(target, newTermsMap):
    for i in range(0,len(expList)):
        if (expList[i] <= target[0]):
            # Add the DP to to the children list
            newTermsMap[target[0]-expList[i]] = target[1] + 1

def min_terms(target, exp):
    # Create the exponent list
    createExpList(target, exp)
    
    # Init useful variables
    global termsMap
    termsMap = {}
    termsMap[target] = 0
    newTermsMap = {}

    # Step through DP as long as no solution found
    while(0 not in termsMap):

        for key,value in termsMap.items():
            # Create DP children for current all children in old DP step
            dpStep((key,value), newTermsMap)

        # Copy new DP step for recursion
        termsMap = newTermsMap.copy()
    return termsMap[0]

print(min_terms(100,3))


