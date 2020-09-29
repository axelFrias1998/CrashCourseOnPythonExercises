class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

class Apple(Fruit):
    pass

class Grape(Fruit):
    pass

granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")

print(granny_smith.color, granny_smith.flavor)
print(carnelian.color, carnelian.flavor)

class Animal:
    sound = ""

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("{sound} I'm {name}! {sound}".format(
            name = self.name,
            sound = self.sound
        ))

class Piglet(Animal):
    sound = "Oink!"

hamlet = Piglet("Hamlet")
hamlet.speak()

class Cow(Animal):
    sound = "Mooo"

milky = Cow("Milky White")
milky.speak()