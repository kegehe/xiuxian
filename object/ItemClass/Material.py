from object.ItemClass.Item import Item


class Material(Item):
    def __init__(self, name, buy_price, sell_price):
        self.name = name
        self.buy_price = buy_price
        self.sell_price = sell_price
