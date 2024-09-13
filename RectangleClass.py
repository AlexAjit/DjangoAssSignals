class Rectangle: #defined class with the name of Rectangle
    def __init__(self, length: int, width: int): #__init__ it's a methodfor initialization
        
        self.dimensions = {'length': length, 'width': width} #It stores the length and width as a dictionary called dimensions
        self.keys = list(self.dimensions.keys()) 
        self.index = 0

    def __iter__(self): #it's a method to make the Class Iterable meaning that you can use it in a loop.
        return self

    def __next__(self): # it's a method to Handle Iterations 
        if self.index < len(self.keys):
            #it returns a dictionary with the key and its corresponding value.
            key = self.keys[self.index]
            value = self.dimensions[key]
            self.index += 1 #increses by 1
            return {key: value}
        raise StopIteration #If there are no more keys, it requests means raises StopIteration to stop the loop.

    #It returns a string like Rectangle(length, width) when you call print(rect). This is useful for readability during debugging or displaying information about the object.
    def __repr__(self): #it's a method for Displaying data in the way we want.
        return f"Rectangle({self.dimensions['length']}, {self.dimensions['width']})"

rectangle_data = Rectangle(14, 31) 
for data in rectangle_data:
    print(data)

print(rectangle_data)