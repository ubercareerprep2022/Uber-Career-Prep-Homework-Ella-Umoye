class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
class Tree:
    def __init__(self, data):
        # Initialize the tree by creating the root node
        self.root = Node(data)
    
    def add_left_child(self, data):
        # Adds a left child to the root_node if no left_child 
        new_node = Node(data)
        if self.root.left_child == None:
            self.root.left_child = new_node
        # or to a sub_tree of the root_node
        else:
            # create a temp var that's assigned to self.root
            current_node = self.root
            # iterate through it until it reachges a node where the left child is null
            while current_node.left_child != None:
                current_node = current_node.left_child
            # if it sees a Node with a nontype left child it creates a new_node
            current_node.left_child = new_node
            
    def add_right_child(self, data):
        new_node = Node(data)
        if self.root.right_child == None:
            self.root.right_child = new_node
        else:
            # create a temp var that's assigned to self.root
            current_node = self.root
            # iterate through it until it reachges a node where the right child is null
            while current_node.right_child != None:
                current_node = current_node.right_child
            # if it sees a Node with a nontype right child it creates a new_node
            current_node.right_child = new_node
    def print(self):
        """Implement a method called print() to print the values of the data in all 
        the TreeNodes in a Tree above. For example, running print() on the Tree above
        should produce one of the three values below:
        1 7 17 6 3
        7 1 6 17 3
        7 6 3 17 1"""
        if self.root == None:
            return
        # Using a queue, simply iterate through the tree
        queue = []
        # starting from root, append to the tree
        queue.append(self.root)
        # while the len(queue) > 0, non empty queue
        while len(queue) > 0:
            # print(the queue and dequeue)
            print(queue[0].data)
            current_node = queue.pop(0)
            # if current_node isn't None:
            # append the node at the left child to the queue
            if (current_node.left_child != None):
                queue.append(current_node.left_child)
            # if current_node isn't None:
            # append the node at the right child to the queue
            if(current_node.right_child != None):
                queue.append(current_node.right_child)

    def printLevelByLevel(self):
        # ensures the tree isn't empty
        if self.root == None:
            return
        current_node = self.root
        queue = []
        queue.append(self.root)
        while queue:
            queue_len  = len(queue)
            count = 0
            while(queue_len>0):
                current_node = queue.pop(0)
                # print(f"{count} tree node ")
                count += 1
                print(f"{current_node.data}", end=" ")
                # check that the left child isn't none and append the subtree to the queue
                if current_node.left_child != None:
                    queue.append(current_node.left_child)
                # check that the right child isn't none and append the subtree to the queue
                if current_node.right_child != None:
                    queue.append(current_node.right_child) 
                queue_len -= 1
            print(' ')
    
    def printNumLevels(self):
        # ensures the tree isn't empty
        if self.root == None:
            return
        current_node = self.root
        queue = []
        queue.append(self.root)

        while queue:
            queue_len  = len(queue)
            count = 0
            while(queue_len>0):
                current_node = queue.pop(0)
                # print(f"{count} tree node ")
                count += 1
                # print(f"{current_node.data}", end=" ")
                # check that the left child isn't none and append the subtree to the queue
                if current_node.left_child != None:
                    queue.append(current_node.left_child)
                # check that the right child isn't none and append the subtree to the queue
                if current_node.right_child != None:
                    queue.append(current_node.right_child) 
                queue_len -= 1
            # print(' ')
        return count

def test_tree_print():
    root = Tree(45)
    root.add_left_child(80)
    root.add_right_child(19)
    root.add_left_child(20)
    root.print()
# test_tree_print(): some behavior, prints it on separate lines than one single line

def test_tree_print_level_by_level():
    root = Tree(1)
    root.add_left_child(3)
    root.add_left_child(6)
    root.add_left_child(6)
    root.add_right_child(5)
    root.add_left_child(6)
    root.add_right_child(20)
    root.add_left_child(14)
    root.add_right_child(55)
    root.add_left_child(17)
    root.add_right_child(81)
    root.add_left_child(89)
    root.add_right_child(11)
    root.add_left_child(4)
    root.add_right_child(0)
    root.add_left_child(100)
    root.add_right_child(22)
    root.add_left_child(15)
    root.add_right_child(10)

    print("Level Order Traversal of binary tree is -")
    # root.printLevelByLevel()
    print(root.printLevelByLevel())
test_tree_print_level_by_level()