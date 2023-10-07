import random

level_dict = {
    'lv1': {'efficiency': 10, 'lower limit': 0, 'upper_limit': 1000, 'success_rate': 1},
    'lv2': {'efficiency': 20, 'lower limit': 1000, 'upper_limit': 2000, 'success_rate': 0.9},
    'lv3': {'efficiency': 30, 'lower limit': 2000, 'upper_limit': 3000, 'success_rate': 0.8},
    'lv4': {'efficiency': 40, 'lower limit': 3000, 'upper_limit': 4000, 'success_rate': 0.7},
}


def update():
    now_efficiency = 0
    now_level = 'lv1'
    data = level_dict[now_level]
    if now_efficiency >= data['upper_limit']:
        ...
    now_efficiency += int(random.uniform(0.7, 1.3) * 20)  # 在0.7到1.3范围内随机




