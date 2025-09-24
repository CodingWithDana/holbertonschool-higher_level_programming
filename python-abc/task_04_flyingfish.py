class Fish:
    def swim(self):
        print("The fish is swimming")
    
    def habitat(self):
        print("The fish lives in water")


class Bird:
    def fly(self):
        print("The bird is flying")
    
    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    def swim(self):
        print("The flying fish is swimming!")
        
    def fly(self):
        print("The flying fish is soaring!")
        
    def habitat(self):
        print("The flying fish lives both in water and the sky!")
        
# instantiate
flying_fish = FlyingFish()
# call methods: fly, swim, habitat
swim(flying_fish)
fly(flying_fish)
habitat(flying_fish)

# use mro() method
print(FlyingFish.mro())

# or can use .__mro__ attribute on FlyingFish class
# print(FlyingFish.__mro__)
