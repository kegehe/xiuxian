from object.ItemClass.Material import Material


class Businessmen:
    def __init__(self, name, businessmen_type):
        self.name = name
        self.businessmen_type = businessmen_type
        self.money = 1000
        # 根据商人类型不同，随机不同的物品
        if businessmen_type == '':
            self.goods = {
                '1': {'id': 1, 'thing': 1, 'num': 20},
                '2': {'id': 2, 'thing': 1, 'num': 20},
                '3': {'id': 3, 'thing': 1, 'num': 20},
            }
        elif businessmen_type == '':
            self.goods = {
                '1': {'id': 1, 'thing': 1, 'num': 20},
                '2': {'id': 2, 'thing': 1, 'num': 20},
                '3': {'id': 3, 'thing': 1, 'num': 20},
            }

    # 商人卖出东西，金钱增加，按物品的买入价格卖出
    def sell_item(self, item):
        sell_good = self.goods[item]
        self.money += sell_good['thing'].sell_price
        sell_good['num'] -= 1
        return item

    # 商人收购东西，金钱减少，按物品的卖出价格买入
    def buy_item(self, index):
        if index not in self.goods:
            self.goods[index] = 1
        else:
            self.goods[index]['num'] += 1

    # 商人死亡，爆出大部分物品，人物减少声望
    def die(self):
        pass
