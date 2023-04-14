class Equipment:
    def __init__(self, name, material_id, unique_id, atk, defensive, equipment_type, buy_price,
                 sell_price):
        self.material_id = material_id
        self.unique_id = unique_id
        self.name = name
        self.atk = atk
        self.defensive = defensive
        self.equipment_type = equipment_type
        self.buy_price = buy_price
        self.sell_price = sell_price

    # 装备磨损
    def worn(self):
        pass

    # 装备强化
    def enhance(self):
        pass
