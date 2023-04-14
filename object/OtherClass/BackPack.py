class BackPack:
    max_weight = 100
    now_weight = 0
    contains = {}

    def expand(self):
        pass

    def pack_in(self, item):
        if self.now_weight >= 1.2 * self.max_weight:
            print('can not carry any more')
        else:
            if item.unique_id not in self.contains:
                self.contains[item.unique_id] = {'item': item, 'num': 1}
            else:
                self.contains[item.unique_id]['num'] += 1
            self.max_weight += item.weight

    def pack_out(self, item):
        if item.unique_id in self.contains:
            if self.contains[item.unique_id]['num'] <= 1:
                del self.contains[item.unique_id]
            else:
                self.contains[item.unique_id]['num'] -= 1
        else:
            print('不存在')
