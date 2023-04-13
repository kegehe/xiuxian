import pickle
import time

from object.Character import Character

from object.Enemy import Enemy


def get_data():
    with open("./static/character.pickle", "rb") as f:
        obj = pickle.load(f)
    return obj


# 战斗
def fight(obj1: Character, obj2: Enemy):
    while obj1.HP > 0 and obj2.HP > 0:
        obj1.HP -= obj2.atk
        obj2.HP -= obj1.atk
        time.sleep(1)
    if obj2.HP < 0:
        m = obj2.die()
        obj1.back_pack.append(m)
    else:
        obj1.die()
    obj1.get_status()


character = Character('java')
enemy = Enemy()
fight(character, enemy)
