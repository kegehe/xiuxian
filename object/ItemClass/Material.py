
class Material:
    def __init__(self, name, material_id, unique_id, buy_price, sell_price):
        self.material_id = material_id
        self.unique_id = unique_id
        self.name = name
        self.buy_price = buy_price
        self.sell_price = sell_price

    # TODO: 物品增加过期时间
