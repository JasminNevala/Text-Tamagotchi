from random import randrange

"""This is for testing, if there's problems with importing in Pycharm"""


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

    def __str__(self):
        return """ {}.\n""".format(self.name)


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


class Consumable:
    """A base class for foods"""

    def __init__(self, name, healing_value):
        self.name = name
        self.healing_value = healing_value

    def __str__(self):
        return "{} ({})".format(self.name, self.healing_value)


class IceCream(Consumable):
    def __init__(self):
        super().__init__(name="Ice Cream", healing_value=5)


class Bamboo(Consumable):
    def __init__(self):
        super().__init__(name="Bamboo", healing_value=3)


class Chocolate(Consumable):
    def __init__(self):
        super().__init__(name="Chocolate", healing_value=2)


class Toy:
    """A base class for toys"""

    def __init__(self, name, mood_value):
        self.name = name
        self.mood_value = mood_value

    def __str__(self):
        return "{}".format(self.name)


class Ball(Toy):
    def __init__(self):
        super().__init__(name="A Ball", mood_value=4)


class Stick(Toy):
    def __init__(self):
        super().__init__(name="A stick", mood_value=2)


def print_foods():
    foods = [IceCream(), Bamboo(), Chocolate()]
    for i, item in enumerate(foods, 1):
        print("{}. {}".format(i, item))


def print_toys():
    toys = [Ball(), Stick()]
    for i, item in enumerate(toys, 1):
        print("{}. {}".format(i, item))


def print_pets():
    pet_list = list_of_pets
    for i, item in enumerate(pet_list, 1):
        print("{}. {}".format(i, item))


def choose_pet():
    pet_list = list_of_pets
    print("Choose a pet: ")
    print_pets()
    choice = input("")
    try:
        chosen_pet = pet_list[int(choice) - 1]
        pet_name = chosen_pet.name
        print("You chose {}!".format(pet_name))
        player_pet = chosen_pet
        return player_pet
    except(ValueError, IndexError):
        print("Invalid choice, try again.")


def print_statistics(self):
    all_stats = ([('Name:', self.name), ('Health:', self.health), ('Boredom: ', self.boredom), ('Mood: ', self.mood),
                  ('Hunger: ', self.hunger)])

    for key, value in all_stats:
        print(key, value)


def feed(self):
    foods = [IceCream(), Bamboo(), Chocolate()]
    print("Your pet's health is {}".format(self.health))
    print("Choose a food: ")
    print_foods()
    choice = input("")
    try:
        to_eat = foods[int(choice) - 1]
        self.health = self.health + to_eat.healing_value
        print("Current health: {}".format(self.health))
    except(ValueError, IndexError):
        print("Invalid choice, try again.")


def play(self):
    toys = [Ball(), Stick()]
    print("Your pet's mood is {}".format(self.mood))
    print("Choose a toy: ")
    print_toys()
    choice = input("")
    try:
        to_play = toys[int(choice) - 1]
        self.mood = self.mood + to_play.mood_value
        print("Your pet's mood increased to {}".format(self.mood))
    except(ValueError, IndexError):
        print("Invalid choice, try again.")


def pet(self):
    petting_value = 2
    self.mood = self.mood + petting_value
    print("You petted your {}. It loved it!".format(self.name))
    print("{}'s mood is now {}".format(self.name, self.mood))


list_of_pets = [Panda(), Kitten(), Tardigrade()]


def clock_ticks(self):
    """ Randomly decrease stats """
    self.boredom -= randrange(1 - 3)
    self.health -= randrange(1 - 5)
    self.mood -= randrange(1 - 3)
    self.hunger -= randrange(1 - 4)


def play_game():
    i = 2
    while i == 2:
        player_animal = choose_pet()
        print_statistics(player_animal)
        i -= 1


play_game()
