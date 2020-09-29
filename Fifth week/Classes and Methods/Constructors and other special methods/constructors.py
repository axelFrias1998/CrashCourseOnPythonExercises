class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

jonagold = Apple("Red", "Sweet")
print(jonagold.color, jonagold.flavor)
print(jonagold)