from constants import ARMORS


class Armor:
    def __init__(self, name, level):
        self.name = name
        self.slot = 2
        self.level = level
        self.protection = ARMORS[self.name][0] + ARMORS[self.name][1] * (self.level - 1)
