import pickle
import random
import time

import data
from object.ItemClass.Equipment import Equipment
from object.OtherClass.BackPack import BackPack


class Character:
    # 基本信息
    name = ''
    big_lever = '炼器期'
    small_lever = '第一层'
    # 基本属性
    max_hp = 100
    now_hp = max_hp
    base_mp = 100
    now_mp = 100
    exp = 0
    cure_rate = 1.0
    # 攻击防御属性
    base_atk = 10
    now_atk = base_atk
    base_defensive = 1
    now_defensive = base_defensive
    # 装备
    equipment_head: Equipment = None
    equipment_shoes: Equipment = None
    equipment_cloth: Equipment = None
    equipment_pants: Equipment = None
    # 其他属性
    money = 0  # 货币
    # meditate_rate = 1.0  # 随时间恢复，特性，不同角色打坐效率不同，减少的效率也不同
    efficiency = 1  # 每次增加的修为值
    reputation = 0  # 声望，击杀中立生物及NPC减少声望，击杀悬赏怪物或负声望值敌人增加声望，声望影响商店购买价格，声望过商店将拒绝售卖商品，且商人会主动攻击人物
    # 背包
    back_pack = BackPack()

    def __init__(self, name):
        self.name = name

    def meditate(self):
        flag = True
        while flag:
            self.exp += self.efficiency

    # 回复状态，可通过打坐或药物回复，打坐回复与恢复率有关
    def cure(self):
        if self.now_hp <= self.max_hp:
            self.now_hp += 1

    # 突破境界，各个境界突破概率不同，可通过丹药或奇遇提升突破概率
    def breakthrough(self):
        breakthrough_rate = data.BREAKTHROUGH_RATE[self.big_lever][self.small_lever]
        if random.random() < breakthrough_rate:
            self.exp *= 0.7
        else:
            self.max_hp *= 1.2
            self.small_lever = 1
            self.efficiency = 1.2
            self.base_atk = 1.2
            self.base_defensive = 1.2

    # 获取人物状态
    def get_status(self):
        character_status = {
           self
        }

    # 人物死亡，随机掉落背包或装备槽一格物品，装备槽物品掉落概率较低，损失3成当前境界修为
    def die(self):
        pass

    # 保存角色信息
    def save_character(self):
        with open("../../static/character.pickle", "wb") as f:
            pickle.dump(self, f)

    # 装备装备
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

    # 人物售卖物品，金钱增加，按物品的卖出价格卖出
    def sell_item(self, index):
        pass

    # 人物买入物品，金钱减少，按物品的买入价格买入
    def buy_item(self, index):
        pass
