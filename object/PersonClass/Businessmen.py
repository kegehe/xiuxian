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

    def sell_item(self, index):
        sell_good = self.goods[index]
        self.money += sell_good['thing'].sell_price
        sell_good['num'] -= 1

    def buy_item(self, index):
        if index not in self.goods:
            self.goods[index] = 1
        else:
            self.goods[index]['num'] += 1


b = Businessmen()
b.sell_item('1')
print(b.money)
