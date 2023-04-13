import pickle
import random
import time

import data


class Character:
    # 基本信息
    __name = ''
    __big_lever = '炼器期'
    __small_lever = '第一层'
    # 基本属性
    HP = 100
    __exp = 0
    __efficiency = 1    # 随时间恢复，特性，不同角色打坐效率不同，减少的效率也不同
    __title = '肉身凡胎'
    atk = 10
    # 装备
    __equipment_head = None
    __equipment_shoes = None

    meditate_rate = 1.0

    back_pack = []

    def __init__(self, name):
        self.__name = name

    # 不能长时间打坐
    def meditate(self):
        flag = True
        t = 0
        while flag:
            time.sleep(1)
            self.__exp = round((self.__exp + self.__efficiency * self.meditate_rate), 2)
            # 效率过低
            t += 1
            if t % 10 == 0:
                self.meditate_rate -= 0.1
            if self.meditate_rate <= 0.5:
                flag = False
                print('tried')
            print(f'exp: {self.__exp}')

    def breakthrough(self):
        breakthrough_rate = data.RATE[self.__big_lever][self.__small_lever]
        print(breakthrough_rate)

    def get_status(self):
        print(self.__name)
        print(self.__exp)
        print(f'{self.__big_lever}{self.__small_lever}')
        print(self.back_pack)

    def die(self):
        lost_item = random.choice(self.back_pack)
        self.back_pack.remove(lost_item)

    # 保存角色信息
    def save_character(self):
        with open("../static/character.pickle", "wb") as f:
            pickle.dump(self, f)
