class dog:
    name = None
    breed = None
    height = None
    weight = None
    race = None

    def __init__(self, nameGiven, breedGiven):
        print("inside parameter constructor")
        self.name = nameGiven
        self.breed = breedGiven

    def bark(self):
        print("Barking")

    def sleep(self):
        pass


chow = dog("chow", "mastiff")
chow.bark()
chow.sleep()

rancho = dog("rancho", "abc")
rancho.bark()
rancho.sleep()
print("Rancho race:", rancho.race)
