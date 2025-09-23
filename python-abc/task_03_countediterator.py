class CountedIterator:
    def __init__(self, iterable):
        # create the iterator object
        self.iterator = iter(iterable)
        # initialise the counter
        self.__count = 0
  
    def get_count(self):
        return self.__count

    # overwite the __next__ meth    od
    def __next__(self):
        # try to fetch the try to next item from the orginal itertor
        try:
            next_item = next(self.iterator)
            self.__count += 1
            return next_item
        except StopIteration:
            # no more items left to iterate
            raise

# instantiate
data = [1, 2, 3, 4]
ci = CountedIterator(data)

# manually iterate using __next__
print(next(ci))  # prints 1
print(next(ci))  # prints 2
print("Items fetched so far ", ci.get_count())  # prints 2 (no. items already printed)
