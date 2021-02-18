from random import randint as ri


class Entity:
    def __init__(self, level, hp, fraction, coordinates, inventory, inventory_size,
                 melee_slot, armor_slot, after_death_items, exp):
        self.level = level
        self.lp = 0
        self.hp = hp
        self.fraction = fraction
        self.coordinates = coordinates
        self.inventory = inventory
        self.inventory_size = inventory_size
        self.slots = [melee_slot, armor_slot]
        self.after_death_items = after_death_items
        self.exp = exp

    def to_attack(self, field, target_coordinates):
        self.hp = self.hp
        return True

    def to_drop_items_after_death(self):
        items = []
        for i in self.after_death_items:
            if ri(0, 101) <= i[1]:
                items.append(i[0])
        return items

    def to_get_damage(self, hp):
        self.hp -= hp
        if self.hp <= 0:
            self.to_drop_items_after_death()
            return False
        else:
            return True
