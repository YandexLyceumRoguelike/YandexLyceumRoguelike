from constants import WEAPONS


class Weapon:
    def __init__(self, name, level):
        self.name = name
        self.slot = 0
        self.level = level
        self.damage = (WEAPONS[self.name][0][0] + WEAPONS[self.name][2] * (self.level - 1),
                       WEAPONS[0][1] + WEAPONS[self.name][2] * (self.level - 1))
        self.number_of_hits = WEAPONS[1]
