from random import randint as ri
from constants import FIELD_SIZE
from Entities.Player import Player
from Entities.Entity import Entity
from Items.Armor import Armor
from Items.Weapon import Weapon


def generation(level, player):
    map = []
    for i in range(FIELD_SIZE[0]):
        map.append([""] * FIELD_SIZE[1])
    portal_coordinates = ri(0, FIELD_SIZE[0]), ri(0, FIELD_SIZE[1])
    portal = [["Стена", "Стена", "Стена", "Стена", "Стена", "Стена", "Стена"],
              ["Стена", "Пол", "Пол", "Портал", "Пол", "Пол", "Стена"],
              ["Стена", "Пол", "Пол", "Пол", "Пол", "Пол", "Стена"],
              ["Стена", "Пол", "Пол", "Пол", "Пол", "Пол", "Стена"],
              ["Стена", "Стена", "Стена", "Стена", "Стена", "Стена", "Стена"]]
    The_Hero_of_Sovngarde = Entity(level, 100, "Heroes of Sovngard", (-1, -1), [], 5,
                                   Weapon("Нордский меч", level), Armor("Нордская броня", level),
                                   [], 0)

    return map
