import random
# 生态问题
dic = {
    'a':0.1,
    'b':0.2,
    'c':0.7,
}
item = list(dic.keys())
probability = list(dic.values())
x = random.choices(item,weights=probability, k=1)

print(x)
