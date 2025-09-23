class VerboseList(list):
    def append(self, item):
        # call the append of the real list
        super().append(item)
        print(f"Added {item} to the list.")
        
    def extend(self, item):
        super().extend(item)
        print(f"Extended the list with len({item}) items.")
        
    def remove(self, item):
        print(f"Removed {item} from the list.")
        super().remove(item)
        
    def pop(self, index=-1):
        print(f"Popped {index} from the list.")
        super().pop(index)
        
# Instantiate
vl = VerboseList([1, 2, 3])

# Tests
vl.append(4) # print 4
vl.extend([5, 6]) 
vl.remove(2)
popped_item = vl.pop()
