from ctypes import sizeof
from typing import get_type_hints

class SingleNumber:
    def __init__(self, name = "name", number = 0):
        self.key = None
        self.left = None
        self.right = None
        self.name:str = name
        self.number:int = number
    
    
class BinarySearchTreePhoneBook:
    def __init__(self, name = "name", number = 0):
        self.root = SingleNumber(name, number)

    def insert(self, name, phone_number):
        if self.root == None:
            self.root.name = name
            self.root.number = phone_number
        else:
            current_node = self.root
            while current_node != None:
                if name < current_node.name:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = SingleNumber()
                        current_node.left.name = name
                        current_node.left.number = phone_number
                        break
                
                if name > current_node.name:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = SingleNumber()
                        current_node.right.name = name
                        current_node.right.number = phone_number
                        break
    def find(self, name):
        if not self.root:
            return
        current_node = self.root
        while current_node:
            if name < current_node.name:
                if current_node.left:
                    current_node = current_node.left
                else:
                    break
            elif name > current_node.name:
                if current_node.right:
                    current_node = current_node.right
                else:
                    break
            elif current_node.name ==  name:
                return f"The number associated with this name: {current_node.name} is: {current_node.number}"
            else:
                break
        return f"The name {name}, does not exist in the directory"
    def printLevelByLevel(self):
        if self.root == None:
            return 
        queue = []
        queue.append(self.root)
        while queue:
            queue_len = len(queue)
            while queue_len:
                current_node = queue.pop(0)
                print(f"Name: {current_node.name}, phone number: {current_node.number}", end= " ")
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
                queue_len -= 1
            print(" ")
    
    def size(self):
        if self.root is None:
            return 0
        queue = []
        queue.append(self.root)
        count = 1
        while(len(queue)!=0):
            curr_node = queue.pop(0)
            if curr_node.left:
                queue.append(curr_node.left)
                count += 1
            if curr_node.right:
                queue.append(curr_node.right)
                count += 1
        return count

root = BinarySearchTreePhoneBook("ABC", 1111111111)
root.insert("BCD", 2222222222)
root.insert("XYZ", 9999999999)
root.insert("DEF", 4444444444)
print(root.find("DEF"))
print(root.find("GHI"))
print(root.size())
root.printLevelByLevel()
# root.printLevelByLevel()
#{"name": "ABC", "phoneNumber": 1111111111}
#  * {"name": "XYZ", "phoneNumber": 9999999999}
#  * {"name": "DEF", "phoneNumber": 2222222222}
#  *