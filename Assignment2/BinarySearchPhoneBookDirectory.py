import csv
import time

class BookDetails:
    def __init__(self, name = "name", number = 0):
        self.name = name
        self.number = number
        self.left = None
        self.right = None
    

class BianrySearchPhoneBookDir:
    def __init__(self):
        self.root = BookDetails()
    
    def insert(self, file):
        start_time = time.time()
        with open(file) as file_content:
            reader_file = csv.reader(file_content)
            for line in reader_file:
                # print(line)
                if not self.root:
                    self.root.name = line[0]
                    self.number = line[1]
                    # print(self.root.name)
                else:
                    current_dir = self.root
                    while current_dir != None:
                        if line[0] < current_dir.name:
                            if current_dir.left:
                                current_dir = current_dir.left
                            else:
                                current_dir.left = BookDetails()
                                current_dir.name = line[0]
                                current_dir.number = line[1]
                                break
                        
                        if line[0] > current_dir.name:
                            if current_dir.right:
                                current_dir = current_dir.right
                            else:
                                current_dir.right = BookDetails()
                                current_dir.name = line[0]
                                current_dir.number = line[1]
                                break
        end_time = time.time()
        time_in_ms = (end_time - start_time)
        return self.root
    
    def size(self):
        if self.root is None:
            return 0
        queue = []
        queue.append(self.root)
        count = 0
        while(len(queue)!=0):
            curr_node = queue.pop(0)
            if curr_node.left:
                queue.append(curr_node.left)
                count += 1
            if curr_node.right:
                queue.append(curr_node.right)
                count += 1
        return count

    def find(self, file):
        count = 0
        with open(file, "r") as file:
            lines = file.read().split('\n')
        for line in lines:
            if not self.root:
                return
            current_node = self.root
            while current_node:
                if current_node.name ==  line:
                    count += 1
                    print(f"The number associated with this name: {current_node.name} is: {current_node.number}")
                elif line > current_node.name:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        break
                elif line < current_node.name:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        break
                    break
            else:
                print(f"The name {line}, does not exist in the directory")
                break
        return count
                    
                    
root = BianrySearchPhoneBookDir()
(root.insert("data.csv"))
print(root.size())
print(root.find('search.txt'))

                    