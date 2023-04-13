import random


class Enemy:
    __name = 's'
    HP = 20
    atk = 1

    Materials = {
        '1':0.2,
        '2':0.3,
        '3':0.5,
    }

    def die(self):
        item = list(self.Materials.keys())
        probability = list(self.Materials.values())
        print(item)
        material = random.choices(item, weights=probability, k=1)
        return material
