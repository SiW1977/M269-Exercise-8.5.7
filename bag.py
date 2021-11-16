# Initiated by Si Woolley
# Date: 16/11/2021

class Bag:
    """An unordered collection of items, potentially with
        duplicates, based on Python's dict class.
    """
    
    def __init__(self, items: object):
        """Create a new bag with the given items.
        
        Preconditions: items is an iterable collection of hashable objects
        """
        
        self.members = dict()
        for item in items:
            self.add(item)
            
    def add(self, item: object):
        """Adds new item to the bag.
        
        Preconditions: item not null
        Postconditions: 
        
        Steps:
        check if item already exists. If it does:
            add 1 to the value
        else append new item and set value to 1 
        """        
        if self.verify(item):
            self.members[item] = self.members[item] + 1
        else:
            self.members[item] = 1
        
    def verify(self, item: object)-> bool:
        """Checking if item exists in the bag.        
        """
        return item in self.members
    
    
    def __str__(self) -> str:
        """Return a string representation of the bag.

        Postconditions: the output uses Python's syntax for dictionaries
        """
        return str(self.members)