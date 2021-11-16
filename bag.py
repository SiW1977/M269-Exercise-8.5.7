from __future__ import annotations

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
        Postcondtions: member is incremented if found, or added as new if not. 
        """                
        if self.verify(item):
            self.members[item] += 1
        else:
            self.members[item] = 1
            
            
    def remove(self, item: object):
        """removes an item from the bag        
        preconditions: item not null, bag not empty        
        postconditions: item value decremented by 1, or item removed from bag
        """        
        if self.verify(item):
            if self.members[item] > 1:
                self.members[item] -= 1
            else:
                self.members.pop(item)
                
                
    def size(self)-> int:
        """returns the current size of the bag.
        """        
        total = 0
        for count in self.members:
            total += self.members[count]
        return total
    
    
    def intersect(self, bag_right: Bag) -> Bag:
        """returns the intersection of self and another bag.
        preconditions: bag_right is of class bag
        postconditions: returned Bag is equal to the length of total unique items in intersected bags.      
        """
        # Assign values to sets for intersection
        set_left = set(self.members) 
        set_right = set(bag_right.members)
        
        # Compare sizes of both sets. 
        # That with least unique items is intersected by the larger.        
        if len(set_left) <= len(set_right):
            return dict.fromkeys(set_left.intersection(set_right), 1)
        else:
            return dict.fromkeys(set_right.intersection(set_left), 1)
            
        
    def verify(self, item: object)-> bool:
        """Checking if item exists in the bag.        
        """        
        return item in self.members
    
    
    def __str__(self) -> str:
        """Return a string representation of the bag.
        """        
        return str(self.members)