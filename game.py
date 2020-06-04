from random import randrange
import pets
import activities


def clock_ticks(self):
    """ Randomly decrease stats """
    self.boredom -= randrange(1 - 3)
    self.health -= randrange(1 - 5)
    self.mood -= randrange(1 - 3)
    self.hunger -= randrange(1 - 4)


panda = pets.Panda()
activities.print_statistics(panda)

