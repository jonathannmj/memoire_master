from itertools import islice

dic = {
    1 :{"name": "jonathan", 'aka': "the flash"},
    2: {'name': "hermes", 'aka': "savitar"},
    3 :{"name": "jonathan", 'aka': "the flash"}, 
    4: {'name': "hermes", 'aka': "savitar"}}

len = len(dic)
step = len // 3

print(dict(islice(dic.items(), 0, step)))
print(dict(islice(dic.items(), step, step*2)))
print(dict(islice(dic.items(), step*2, len)))
print(len)