class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
    def speak(self):
        """Outputs a message including the name of the piglet."""
        print("Oink! I'm {}! Oink!".format(self.name))

    def pig_years(self):
        """Converts the current age to equivalent pig years."""
        return self.years * 18
        
    def to_seconds(self, hours, minutes, seconds):
        """Returns the amount of seconds in the giben hours, minutes, and seconds."""
        return hours * 3600 + minutes * 60 + seconds

jonagold = Apple("Red", "Sweet")
print(jonagold.color, jonagold.flavor)
print(jonagold)

print(help(jonagold))

print(help(Apple))