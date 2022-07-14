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
        # print(self.dict)
        end_time = time.time()
        insert_time_in_ms = (end_time - start_time) * 1000
        return insert_time_in_ms
    def size(self):
        return len(self.dict) 
    def find(self, file_to_read):
        count = 0
        with open(file_to_read, "r") as file:
            lines = file.read().split('\n')
        for line in lines:
            if line in self.dict:
                count += 1
            else:
                print(self.dict[line])
                count -= 1
        return count
new_phonebook = ListPhoneBookDirectory()
milliseconds = new_phonebook.insert("data.csv")
print(f"Insert took {milliseconds} milliseconds.")
phone_book_size = new_phonebook.size()
print(f"The ListPhoneBookDir is {phone_book_size}")
found = new_phonebook.find("search.txt")
if found == 1000:
    print("All uiuds were found within the phone directory")
else:
    print("There's a bug in your find method :(")

