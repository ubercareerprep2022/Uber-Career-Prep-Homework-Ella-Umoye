# void push(<Node> node) → Adds the node to the end of the list
# <Node> pop() → Removes the last node at the end of the linked list, returns that 
# data void insert(uint index,<Node> node) → Adds a single node containing data to --> should I insert
# At that index or after the index?
# a chosen location in the list. If the index is above the size of the list, do 
# nothing void remove(uint index) → remove/delete a single node at the index location
# in the list. If the node doesn’t exist at the index, do nothing
# <Node> elementAt(uint index) → Returns a pointer to the node at the index location
# in the list. If the node doesn’t exist at the index, return nil/null
# uint size() → Returns the length of the list.
# void printList() → Returns a string representation of the linked list

from cgi import test
from hmac import new
from itertools import count
from os import link
from random import random


class Node:
    def __init__(self, value, link_node = None):
        """Initiliaze the linked list property, node and pointer"""
        self.curr_node = value
        self.next = link_node
    
    def get_value(self):
        """Returns the value of the current_node"""
        return self.curr_node

    def get_link_node(self):
        """A method to return the pointer"""
        return self.next
    
    def set_link_node(self, link_node):
        """A method to set the pointer"""
        self.next = link_node

class linkedList(Node):
    def __init__(self, value=None):
        self.head = Node(value)

    def get_head_node(self):
        """returns the head node"""
        return self.head
    
    def push(self, new_node):
        """ Push to the beginning of the node """
        # Create an object of type node
        new_linked_list = Node(new_node)
        # Assign the pointer the value of the self.head
        new_linked_list.set_link_node(self.head)
        # Set self.head to be the pushed new_node
        self.head = new_linked_list

    def pop(self):
        """Removes and returns the last element at the end of the linkedlist"""
        remove_node = self.head
        # I think I should save the prev_node somewherr
        prev_node = self.head
        # check if the linkedlist is empty and return
        if(self.head == None):
            return 
        # 1->2->3->4 and I pop 4
        # First I'll iterate till I get to 4 which shows end of the list
        # Then I save it in a variable, then I link the prev_node to None and return the removed value
        
        while(remove_node!= None):
            # Check if the last node has been reached
            if(remove_node.next == None):
                # Set prev_node.next to None
                prev_node.next = None
                # Show the node that was removed
                return remove_node.curr_node
            else:
                # Then I set prev_node to the curr_node
                # And curr_node to the next_node making it one step ahead
                prev_node = remove_node
                remove_node = remove_node.next
        
    def insert(self,index, new_node):
        """Inserts an element after the specified element if it exists in the linkedlist"""
        # Inserts an element after the specified index? Or should it replace the lement at that index
        # Identify where the node is 
        # Check if it's next node is none, if yes then set it to the new node, no need for this
        # If it isn't then insert the new node such that it goes from a --> c to a --> b --> c
        # prev_linked_node = Node(prev_node)
        new_linked_node =  Node(new_node)
        curr_index = 0
        temp = self.head
        if(temp.next == None):
            temp.next = new_linked_node
            return 
        while(temp!= None):
            if index == curr_index:
                # Then we want to save the temp.next data
                curr = temp.next
                # Then set temp.next = new_linked_node
                temp.next = new_linked_node
                # Then set the new_linked_node's next value to be the value previously after the old node
                new_linked_node.next = curr
                return f"the new_linked_node {new_linked_node.next} has been added"
            else:
                curr_index += 1
                temp = temp.next
        return "Sorry, the index is greater than the length of the linked list"

    def remove(self, index):
        """Removes an element at the specified index"""
        remove_at_index = self.head
        prev_node = self.head
        # If the index is 0 we want to change the head node so 10-28-40 becomes 28-40
        if(index ==0):
            # set the head_node to be the next element
            self.head = remove_at_index.next
            return f"removed: {prev_node.curr_node}"
        index_count = 0
        while(remove_at_index!=None):
            if index == index_count:
                prev_node.next = remove_at_index.next
                return f"removed: {remove_at_index.curr_node}"
            else:
                index_count += 1
                prev_node = remove_at_index
                remove_at_index = remove_at_index.next
        return f"Sorry, this index: {index} is not in the linkedlist"

    def elementAt(self, index):
        """returns the element at the specified index"""
        curr_node = self.head
        count = 0
        while curr_node:
            if count == index:
                return curr_node.curr_node
            else:
                count += 1
                curr_node = curr_node.next
        return f"Sorry, there is the node {index} doesn't exist"
    def pushToEndOfNode(self, new_node):
        """Pushes a new element to the end of the node"""
        # First create an object of the class Node, which essentially creates a node of data
        new_add_node = Node(new_node)
        # check if the headc node is empty which indicates an empty linkedlist
        if self.head == None:
            self.head = new_add_node
        else:
            # IF IT'S NOT AN EMPTY LINKEDLIST, ITERATER TILL YOU REACH thew end of the linkedlist
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            # Once an empty link/pointer has been rerached, that indicates end of the list
            temp.next = new_add_node

    def size(self):
        curr_node = self.head
        count = 0
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count
    def printList(self):
        string_rep = ""
        # set the current_node to the head node of the list
        current_node = self.head
        # while the curr_node is not None
        while current_node:
            if current_node.next != None:
                string_rep += str(current_node.get_value()) + "-->"
            # move the current node to the next node
            else:
                string_rep += str(current_node.get_value())
            current_node = current_node.get_link_node()
        return string_rep 

    def reversedLinkedList(self):
        """Return the linked list reversed- Iterative version"""
        # 4 iter. curr.next = 3, prev = 3 and f= 4?
        current = self.head #points to the 1st element in the list
        previous = None #points to None initially
        following = current.next # points to the second element
        while current:
            current.next = previous #reverse the link
            previous = current #move previous to the next element
            current = following #move current to the next element
            if following: #if it's not the last element
                following = following.next #move following to the next elementS
        #After the iteration, set self.head to the last element which is previous
        self.head = previous
        
    
newLL = linkedList("a")
newLL.pushToEndOfNode("a")
newLL.pushToEndOfNode("a")
newLL.pushToEndOfNode("b")
newLL.pushToEndOfNode("b")
newLL.pushToEndOfNode("b")
newLL.pushToEndOfNode("c")
newLL.pushToEndOfNode("c")
# print(newLL.reversedLinkedList())
newLL.reversedLinkedList()
print(newLL.printList())

def testPushBackAddsOneNode():
    new_LinkedListEnd = linkedList(10)
    new_LinkedListEnd.pushToEndOfNode(28)
    new_LinkedListEnd.pushToEndOfNode(40)
    print(new_LinkedListEnd.printList())
# testPushBackAddsOneNode()
def testPopBackRemovesCorrectNode():
    new_LinkedListRem = linkedList(5)
    new_LinkedListRem.pushToEndOfNode(20)
    new_LinkedListRem.pushToEndOfNode(35)
    print(new_LinkedListRem.pop())
# testPopBackRemovesCorrectNode()

def testEraseRemovesCorrectNode(index):
    new_LinkedListRem = linkedList(9)
    new_LinkedListRem.pushToEndOfNode(8)
    new_LinkedListRem.pushToEndOfNode(7)
    new_LinkedListRem.remove(index)
    print(new_LinkedListRem.printList())
# testEraseRemovesCorrectNode(2)

def testEraseDoesNothingIfNoNode(index):
    new_LinkedListRem = linkedList(None)    
    print(new_LinkedListRem.remove(index))
# testEraseDoesNothingIfNoNode(100)

def testElementAtReturnNode(index):
    new_LinkedListRem = linkedList(11)
    new_LinkedListRem.pushToEndOfNode(22)
    new_LinkedListRem.pushToEndOfNode(33)
    print(new_LinkedListRem.elementAt(index))
# testElementAtReturnNode(1)

def testElementAtReturnsNoNod(index):
    new_LinkedListRem = linkedList(100)
    new_LinkedListRem.pushToEndOfNode(900)
    new_LinkedListRem.pushToEndOfNode(1000)
    print(new_LinkedListRem.elementAt(index))
# testElementAtReturnsNoNod(29)
# Questions
# 1. Is there a faster way to check the length of the linkedlist asides using a counter
# Because say I have 1000 nodes in my linkedlist, It will take 1000 times to perform that operation to geth the
# length
# 2. Is there a way to check if an index exists in the linkedlist without having to iterate through the list?
# It's not efficient to go thrpough the entire linkedlist when I can just return immediately
