import pickle
import random

import data
from object.ItemClass.Equipment import Equipment


class Character:
    def __init__(self, name):
        lv_dict = data.LV
        self.name = name
        self.lv = 'lv1'
        self.efficiency = lv_dict[self.lv]['efficiency']
        self.cultivation = 0
        self.max = lv_dict[self.lv]['max']
        self.success_rate = lv_dict[self.lv]['success_rate']

    def meditate(self):
        increase = int(random.uniform(0.5, 1.5) * self.efficiency)
        self.cultivation += increase
        return increase

    # 突破
    def breakthrough(self):
        ...
