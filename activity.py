import pickle
import random

import data
from object.PersonClass import Businessmen
from object.PersonClass.Character import Character

from object.PersonClass.Enemy import Enemy


def get_data():
    with open("./static/character.pickle", "rb") as f:
        obj = pickle.load(f)
    return obj


def fight(character: Character, enemy: Enemy):
    while character.now_hp > 0 and enemy.now_hp > 0:
        if character.now_defensive >= enemy.now_atk:
            character_damage = 1
        else:
            character_damage = 1
        if enemy.now_defensive >= character.now_atk:
            enemy_damage = 1
        else:
            enemy_damage = 1
        character.now_hp -= enemy_damage
        enemy.now_hp -= character_damage
    if enemy.now_hp < 0:
        material = enemy.die()
        character.back_pack.pack_in(material)
    else:
        character.die()
    character.get_status()


def explore() -> Enemy:
    enemy_list = data.ENEMY_LIST
    random_key = random.choice(list(enemy_list.keys()))  # 随机选择一个键
    enemy = enemy_list[random_key]  # 获取相应值
    return enemy


def trade(obj1: Character, obj2: Businessmen):
    pass
