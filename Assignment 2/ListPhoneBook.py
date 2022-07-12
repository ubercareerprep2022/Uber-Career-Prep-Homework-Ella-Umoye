from pickletools import long1
from typing import List
import ListPhoneBook
class ListPhoneBook:
    """Implements the methods find, and insert that add to the phonebook directory"""
    def __init__(self):
        self.dict = {}
    
    def insert(self, name:str, phone_number:int):
        self.dict[name] = phone_number
    
    def find(self, name):
        for key in self.dict:
            if key == name:
                return self.dict[key]
        return "not existing in the phonebook directory"
    
    def size(self):
        return len(self.dict)

new_number = ListPhoneBook()
new_number.insert("Emmanuella", 1111111111)
new_number.insert("Osereme", 2222222222)
new_number.insert("Ifeoluwa", 3333333333)
new_number.insert("Iwalewa", 4444444444)
print(new_number.find("Iwalewa"))

