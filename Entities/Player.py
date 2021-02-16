from constants import STARTING_VALUE_OF_LEVEL_VOLUME, INCREMENT_OF_LEVEL_VOLUME
from Entities.Entity import Entity


class Player(Entity):
    def to_fill_in_the_inventory(self, item):
        if self.inventory_size - len(self.inventory) > 0:
            self.inventory.append(item)
            return True
        return False

    def to_drop(self, item):
        return True, self.inventory.pop(self.inventory.index(item))

    def to_get_exp(self, exp):
        volume = STARTING_VALUE_OF_LEVEL_VOLUME + INCREMENT_OF_LEVEL_VOLUME * (self.level - 1)
        self.lp += exp
        if self.lp >= volume:
            self.lp -= volume
            self.level += 1
        return False

    def to_equip(self, item):
        k = item.slot
        equipped_item = self.slots[k]
        self.slots[k] = self.inventory.pop(self.inventory.index(item))
        if equipped_item is not None:
            self.inventory.append(equipped_item)
        return True

    def to_take_off(self, item):
        pass
