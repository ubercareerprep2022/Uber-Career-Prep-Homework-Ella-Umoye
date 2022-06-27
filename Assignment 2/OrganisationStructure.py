from re import template
from tkinter.messagebox import NO


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []

class OrganisationStructure:
    def __init__(self, data):
        self.root = Node(data)
    def add_children_to_root(self, child):
        new_node = Node(child)
        self.root.children.append(new_node)
        # else:
        #     current_node = self.root
        #     while current_node.children != None:
        #         current_node = current_node.children
        #     current_node.children = new_node
        
    def add_children_to_node(self, parent_node, data):
        temp = self.root
        temp = temp.children
        new_node = Node(data)
        for i in temp:
            if i.data == parent_node:
                i.append(new_node)
        # while temp.data != parent_node:
        #     temp = temp.children
        
    def printNode(self):
        if self.root == None:
            return
        queue = []
        queue.append(self.root)
        current_node = queue.pop(0)
        print(current_node.data)
        queue.append(self.root.children)
        queue_len = len(queue)
        while queue_len > 0:
            current_node = queue.pop(0)
            print(current_node.data)
            if len(current_node.children ) != 0:
                queue.append(current_node.children)
        print(' ')
root = OrganisationStructure(70)
root_child_one = OrganisationStructure(50)
one_of_child_one = OrganisationStructure(80)
two_of_child_one = OrganisationStructure(100)
root.add_children_to_root(root_child_one)
root_child_one.add_children_to_node(50, 100)
root_child_one.add_children_to_node(50, 80)
print(root.printNode())
    # def printNumLeveles(self):
    #     if self.root == None:
    #         return
    #     queue = []
    #     queue.append(self.root)
    #     temp_node = self.root
    #     count = 0
        
    #     while queue:
    #         len_of_queue = len(queue)
    #         while len_of_queue > 0:
    #             temp_node = queue.pop(0)
    #             count += 1
    #             if (temp_node.children) != None:
    #                 print(temp_node.children)
    #             queue.append(temp_node.children)
    #             len_of_queue -= 1
    #         # print(count)
