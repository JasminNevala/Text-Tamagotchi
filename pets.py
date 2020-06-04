from random import randrange


class Pet:
    """A base class for all the pets"""
    boredom_threshold = 10
    health_threshold = 15
    mood_threshold = 10
    hunger_threshold = 12

    def __init__(self, name):
        self.name = name
        self.boredom = randrange(self.boredom_threshold)
        self.health = randrange(self.health_threshold)
        self.mood = randrange(self.mood_threshold)
        self.hunger = randrange(self.hunger_threshold)

    def __str__(self):
        return """Hi! My name is {}.""".format(self.name)


class Panda(Pet):
    def __init__(self):
        super().__init__(name="Panda")


class Kitten(Pet):
    def __init__(self):
        super().__init__(name="Kitten")
