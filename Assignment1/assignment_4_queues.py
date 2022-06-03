class Queue:
    """Creates a queue data structure from scratch that utilizes
    first-in first-out method"""
    def __init__(self, arr):
        self.arr = arr
    
    def contentQueue(self):
        """Returns the queue"""
        return self.arr
    def enqueue(self, x):
        """Adds the element to the end of the queue"""
        enqueuedVal = self.arr[len(self.arr)-1]
        newArr = [0] * (len(self.arr) + 1)
        for i in range(1, len(self.arr)+1):
            newArr[i] = self.arr[i-1]
        newArr[0] = x
        self.arr = newArr
        # print(f"This {x} number has been added to the queue")
        return self.arr
    
    def dequeue(self, y):
        """Removes the last element in the queue"""
        if y > len(self.arr):
            return "Sorry, that's an index out of range"
        else:
            self.arr.remove(y)
            # print(self.arr)
            # print(len(self.arr))
            # newArr = [0] * (len(self.arr) - 1) 
            # for i in range(1, len(self.arr)-2):
            #     newArr[i-1] = self.arr[i]
            # self.arr = newArr
            # print(f"This {y} number has been removed from the queue")
        return self.arr

    def rear(self):
        """Returns the last element in the queue"""
        return (self.arr[len(self.arr)-1])
    def front(self):
        """Returns the first element in the queue"""
        return (self.arr[0])
    def isEmpty(self):
        """Returns true if the queue is empty"""
        i = 0
        if(len(self.arr)==0):
            print(True)
        else:
            print(False)
        
myQueue = Queue([1,2,3,4,5])
# print(myQueue.dequeue(5))
print(myQueue.contentQueue())
print(myQueue.enqueue(10))
print(myQueue.rear())
print(myQueue.front())
myQueue.isEmpty()