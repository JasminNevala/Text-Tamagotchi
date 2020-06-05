from random import randrange
import activities
import pets

list_of_pets = [pets.Panda(), pets.Kitten(), pets.Tardigrade()]


def clock_ticks(self):
    """ Randomly decrease stats """
    self.boredom -= randrange(1 - 3)
    self.health -= randrange(1 - 5)
    self.mood -= randrange(1 - 3)
    self.hunger -= randrange(1 - 4)


def play_game():
    i = 2
    while i == 2:
        player_animal = activities.choose_pet()
        activities.print_statistics(player_animal)
        i -= 1

play_game()