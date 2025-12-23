class Dog:
    # Attribute
    name = None
    breed = None
    height = None
    weight = None

    def bark(self):
        print("bark")
        # print(name)
        print(self.name)


print("outside?")

lab = Dog()
rancho = Dog()
lab.bark()
rancho.bark()
