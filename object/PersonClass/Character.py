import pickle
import random
import time

import data
from object.ItemClass.Equipment import Equipment


class Character:
    # 基本信息
    name = ''
    big_lever = '炼器期'
    small_lever = '第一层'
    # 基本属性
    max_HP = 100
    now_HP = 100
    exp = 0

    base_atk = 10
    now_atk = base_atk
    base_defensive = 1
    now_defensive = base_defensive

    # 装备
    equipment_head: Equipment = None
    equipment_shoes: Equipment = None
    equipment_cloth: Equipment = None
    equipment_pants: Equipment = None

    money = 0
    meditate_rate = 1.0
    efficiency = 1  # 随时间恢复，特性，不同角色打坐效率不同，减少的效率也不同

    back_pack = [Equipment()]

    def __init__(self, name):
        self.name = name

    # 不能长时间打坐
    def meditate(self):
        flag = True
        t = 0
        while flag:
            time.sleep(1)
            self.exp = round((self.exp + self.efficiency * self.meditate_rate), 2)
            # 效率过低
            t += 1
            if t % 10 == 0:
                self.meditate_rate -= 0.1
            if self.meditate_rate <= 0.5:
                flag = False
                print('tried')
            print(f'exp: {self.exp}')

    def cure(self):
        if self.now_HP <= self.max_HP:
            self.now_HP += 1

    def breakthrough(self):
        breakthrough_rate = data.RATE[self.big_lever][self.small_lever]
        f = []
        if f:
            self.exp *= 0.7
        else:
            self.max_HP = 1
            self.small_lever = 1
            self.efficiency = 1
            self.base_atk = 1

    def get_status(self):
        print(self.name)
        print(self.exp)
        print(f'{self.big_lever}{self.small_lever}')
        print(self.back_pack)

    def die(self):
        lost_item = random.choice(self.back_pack)
        self.back_pack.remove(lost_item)

    # 保存角色信息
    def save_character(self):
        with open("../../static/character.pickle", "wb") as f:
            pickle.dump(self, f)

    def equip_and_un_equip(self, select_equip: Equipment):
        if select_equip.equipment_type == 'head':
            if not self.equipment_head:
                self.back_pack.append(self.equipment_head)
                self.now_atk -= self.equipment_head.atk
                self.now_defensive -= self.equipment_head.atk
                self.equipment_head = select_equip
            else:
                self.equipment_head = select_equip
            self.now_atk += select_equip.atk
            self.now_defensive += select_equip.defensive
        elif select_equip.equipment_type == 'shoes':
            if not self.equipment_shoes:
                self.back_pack.append(self.equipment_shoes)
                self.equipment_shoes = select_equip
            else:
                self.equipment_shoes = select_equip
        elif select_equip.equipment_type == 'shoes':
            if not self.equipment_shoes:
                self.back_pack.append(self.equipment_shoes)
                self.equipment_shoes = select_equip
            else:
                self.equipment_shoes = select_equip
        elif select_equip.equipment_type == 'shoes':
            if not self.equipment_shoes:
                self.back_pack.append(self.equipment_shoes)
                self.equipment_shoes = select_equip
            else:
                self.equipment_shoes = select_equip
