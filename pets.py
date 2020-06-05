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
        self.health = randrange(8, self.health_threshold)
        self.mood = randrange(self.mood_threshold)
        self.hunger = randrange(8, self.hunger_threshold)
        self.bored = False
        self.sick = False
        self.sad = False
        self.hungry = False
        self.dead = False

    # def __str__(self):
    # return """Hi! My name is {}.\n""".format(self.name)


class Panda(Pet):
    def __init__(self):
        super().__init__(name="Panda")


class Kitten(Pet):
    def __init__(self):
        super().__init__(name="Kitten")


class Tardigrade(Pet):
    def __init__(self):
        super().__init__(name="Tardigrade")


def bored(self):
    if self.boredom < 5:
        self.bored = True


def sick(self):
    if self.health < 5:
        self.sick = True


def sad(self):
    if self.mood < 5:
        self.sad = True


def hungry(self):
    if self.hunger < 5:
        self.hungriness = True


def death(self):
    if self.health > 0 or self.hunger > 0:
        self.dead = True
