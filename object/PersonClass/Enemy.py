import random


class Enemy:
    def __init__(self, name, max_hp, atk, defensive):
        self.name = name
        self.max_hp = max_hp
        self.now_hp = self.max_hp
        self.atk = atk
        self.defensive = defensive
        self.Materials = {
            '1': 0.2,
            '2': 0.3,
            '3': 0.5,
        }

    def die(self):
        item = list(self.Materials.keys())
        probability = list(self.Materials.values())
        print(item)
        material = random.choices(item, weights=probability, k=1)
        return material
