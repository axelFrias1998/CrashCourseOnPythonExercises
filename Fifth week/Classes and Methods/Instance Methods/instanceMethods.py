class Piglet:
    name = "Piglet"
    years = 0

    def speak(self):
        print("Oink! I'm {}! Oink!".format(self.name))

    def pig_years(self):
        return self.years * 18

hamlet = Piglet()
hamlet.years = 2
hamlet.name = "Hamlet"
hamlet.speak()
print(hamlet.pig_years())

petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()