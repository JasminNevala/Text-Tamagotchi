from random import randrange


def clock_ticks(self):
    self.boredom -= randrange(1 - 3)
    self.health -= randrange(1 - 5)
    self.mood -= randrange(1 - 3)
    self.hunger -= randrange(1 - 4)