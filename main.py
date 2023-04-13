import pickle
import time

from object.PersonClass.Character import Character

from object.PersonClass.Enemy import Enemy


def get_data():
    with open("./static/character.pickle", "rb") as f:
        obj = pickle.load(f)
    return obj


def fight(obj1: Character, obj2: Enemy):
    while obj1.now_HP > 0 and obj2.HP > 0:
        obj1.now_HP -= obj2.atk
        obj2.now_HP -= obj1.atk
        time.sleep(1)
    if obj2.HP < 0:
        m = obj2.die()
        obj1.back_pack.append(m)
    else:
        obj1.die()
    obj1.get_status()


def explore():
    pass


def trade():
    pass


character = Character('java')
enemy = Enemy()
fight(character, enemy)
