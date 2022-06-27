from tkinter.messagebox import NO


class Node:
    def __init__(self, parent):
        self.parent = parent
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, data):
        self.root = Node(data)
    
    def insert(self, key):
        new_node = Node(key)
        if self.root == None:
            self.root = Node(key)
        else:
            current_node = self.root        
            while current_node != None:
                if key < current_node.parent:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = new_node
                        break
                elif key > current_node.parent:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = new_node
                        break
    
    def find(self, key):
        # check if it's an empty tree
        if self.root ==  None:
            return
        # if not, assign a temp var to traverse through the tree
        current_node = self.root
        # while the current_node isn't none
        while current_node!=None:
            # If the key being searcjed is < than the parent, then we want to traverse through the left subtree
            if key < current_node.parent:
                # check if the current_node.left isn't None
                if current_node.left:
                    print("Now checking through the left node")
                    current_node = current_node.left
                else:
                    # if it's then you want to break the loop and return false becaiuse that means the node isn't within the tree
                    break
            # if the key being searched is > than the parent, then you want to traverse thriough the right subtree
            elif key > current_node.parent:
                # if the right subtree isn't None, then we update current_node to it
                if current_node.right:
                    print("Now checking through the right node")
                    current_node = current_node.right
                # else., the node doesn't exist in the subtree and we break out of the loop
                else:
                    break
            elif key == current_node.parent:
                return True
            else:
                break
        return False
            
    def printTree(self):
        if self.root == None:
                return
        queue = []
        queue.append(self.root)
        while queue:
            queue_len = len(queue)
            while queue_len > 0:
                current_node  = queue.pop(0)
                print(current_node.parent, end=" ")
                if current_node.left != None:
                    queue.append(current_node.left)
                if current_node.right != None:
                    queue.append(current_node.right)
                queue_len -= 1
            print(" ")

root = BinarySearchTree(45)
root.insert(80)
root.insert(19)
root.insert(20)
root.insert(10)
root.printTree()
print(root.find(2))