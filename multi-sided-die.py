import random


class MSDie:
    def __init__(self, sides):
        self.sides = sides
        self.current_value = self.roll()

    def roll(self):
        self.current_value = random.randrange(1, self.sides+1)
        return self.current_value

    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        return f'MSDie({self.sides}): {self.current_value}'

    def __eq__(self, other):
        return self.current_value == other.current_value

    def __gt__(self, other):
        return self.current_value > other.current_value

    def __ge__(self, other):
        return self.current_value >= other.current_value
