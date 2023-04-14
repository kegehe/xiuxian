import random


class Enemy:
    def __init__(self, name, max_hp, base_atk, base_defensive):
        self.name = name
        self.max_hp = max_hp
        self.now_hp = self.max_hp
        self.base_atk = base_atk
        self.now_atk = base_atk
        self.base_defensive = base_defensive
        self.now_defensive = self.base_defensive
        self.Materials = {
            '1': 0.2,
            '2': 0.3,
            '3': 0.5,
        }

    # 死亡后按爆率爆出材料
    def die(self):
        item = list(self.Materials.keys())
        probability = list(self.Materials.values())
        print(item)
        material = random.choices(item, weights=probability, k=1)
        return material
