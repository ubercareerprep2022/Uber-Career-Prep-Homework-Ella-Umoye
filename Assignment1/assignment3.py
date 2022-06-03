from array import array
from ctypes import sizeof
from lib2to3.pgen2.literals import test
from random import sample
import sys


class Stack:
    """Write a stack class that has the following operations:
    1. Pop, adds a new element to the array from the top where if n = len(array)
    Then n+1  = len(newArr)
    2. Push, Pushes off the first element in the array from the top. Where if n = len(array)
    , then n-1  = len(newArr)
    3. isEmpty: checks if the stack is empty
    4. Returns the last in or top element
    5. Content: returns the stack"""
    

    def __init__(self, data):
       """Initializes the Stack class which takes in a specific data type"""
       self.data = data

    def pop(self):
        """Pops the last element in the stack"""
        poppedVal = self.data.pop()
        return f"This is the popped value: {poppedVal}"

    def push(self, y):
        """Pushes a new element to the top of the stack"""
        data = self.data
        newData = [0] * (len(data) + 1)
        for i in range(len(data)):
            newData[i] = data[i]
        # arr = [] * len(arr) + 1
        newData[-1] = y
        data = newData
        return f"This is the new stack with {y} pushed: {data}"

    def size(self):
        """Returns the size of the stack"""
        lenData = len(self.data)
        return f"The length of the stack is {lenData}"

    def isEmpty(self):
        """Returns true if the stack is empty. Otherwise, it will return False"""
        if(len(self.data == 0)):
            return True
        return False
    
    def topNum(self):
        """Returns the top element in the stack"""
        top_num = self.data[-1]
        return f"This is the number at the top of the stack: {top_num}"
    
    def contentArr(self):
        """returns the content of the stack"""
        return self.data
    
    def minElement(self):
        """Returns the minimum element in the stack"""
        data = self.data
        minNum = sys.maxsize
        for i in data:
            minNum = min(minNum, i)
        return f"This is the minimum number in the stack: {minNum}"


sampleArr = [1,2,3,4,5]
newArr = Stack(sampleArr)
print(newArr.pop())

print(newArr.push(5))

def testFun(sampleArr):
    if type(sampleArr) != list:
        print("Sorry, this stack class cannot operate on this data type")
        exit()
    newArr = Stack(sampleArr)
    userInput = input("""What operation will you like to perform on your stack: ?\n"""
    """push/pop/top/isEmpty/content: """)
    if userInput == "push":
        userPushInput = input("""What number will you like to be pushed to the top of\n"""
        """the stack: """)
        newArr.push(userPushInput)
            
    elif userInput == "pop":
        newArr.pop()

    elif userInput == "top":
        newArr.topNum()
    
    elif userInput == "empty":
        newArr.isEmpty()

    elif userInput == "content":
        print(newArr.contentArr())
    
    else:
        print("""sorry, I don't understand that operation. Try\n
        push/pop/top/isEmpty/content""")


