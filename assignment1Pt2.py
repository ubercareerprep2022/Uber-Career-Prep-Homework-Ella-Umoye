from operator import indexOf


def PairsThatEqualSum(inputArr, target):
    """return an array of tuples that contains pairs of elements of the array 
    that adds up to the target"""
    # define the returning new array
    newArr = []
    pairArr = [0,0]
    #Simply iterate through the old array, resetting, the pair tuple for each iteration
    #Used array instead of tuple for the pairTuple because tuples are immutable
    for i in (inputArr):
        pairArr = [0,0]
        #So as not to return duplicate values, check to see if the subarray[a,b] is
        #already within the newArr
        if target - i in inputArr and [target-i, i] not in newArr:
            #To prevent the adding of an element by itself, check to make sure
            #the indexes aren't the same, e.g [1,2,3], 4 => [[3,1], [2,2]] even 
            #tho 2 is itself and not a new element.
            if indexOf(inputArr, target-i) != indexOf(inputArr, i):
                pairArr[0] = i
                pairArr[1] = target - i
                print(target-i)
                newArr.append(pairArr)
    return newArr
print(PairsThatEqualSum([1,2,3,4,5], 5))
        # for j in range(len(inputArr))