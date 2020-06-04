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
