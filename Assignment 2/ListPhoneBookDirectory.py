"""In the first version of the program, the PhoneBook will be a ListPhoneBook.
In the second version of the program, the PhoneBook will be a 
BinarySearchTreePhoneBook.
Read each line of data.csv and insert() it into the PhoneBook created. 
Print out the total time (in milliseconds) it takes to insert() 
a million name and phone number entries.
"""
import csv
import time

class ListPhoneBookDirectory:
    def __init__(self, value={}):
        self.dict = value
    def insert(self, file):
        start_time = time.time()
        with open(file) as file_content:
            reader_file = csv.reader(file_content)
            for line in reader_file:
                self.dict[line[0]] = line[1]
        print(self.dict)
        end_time = time.time()
        insert_time_in_ms = (end_time - start_time) * 1000
        return insert_time_in_ms
    def size(self):
        return len(self.dict) 
    def find(self, file_to_read):
        count = 0
        with open(file_to_read, "r") as file:
            lines = file.read().split('\n')
        # for line in lines:
        #     #print(line)
        #     if self.dict[line] in self.dict.values:
        #         count += 1
        #     else:
        #         print(line)
            # # # print(line)
            # # if line in self.dict:
            # #     print(line)
            # # else:
            # #     continue
        return count
new_phonebook = ListPhoneBookDirectory()
print(new_phonebook.insert("data.csv"))
# print(new_phonebook.size())
print(new_phonebook.find("search.txt"))
