import game
import items


def print_foods():
    foods = [items.IceCream(), items.Bamboo(), items.Chocolate()]
    for i, item in enumerate(foods, 1):
        print("{}. {}".format(i, item))


def print_toys():
    toys = [items.Ball(), items.Stick()]
    for i, item in enumerate(toys, 1):
        print("{}. {}".format(i, item))


def print_pets():
    pet_list = game.list_of_pets
    for i, item in enumerate(pet_list, 1):
        print("{}. {}".format(i, item))


def choose_pet():
    pet_list = game.list_of_pets
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
    foods = [items.IceCream(), items.Bamboo(), items.Chocolate()]
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
    toys = [items.Ball(), items.Stick()]
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


