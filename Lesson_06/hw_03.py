# Созадать словарь в качестве ключа которого будет 6-ти значное число,
# а в качестве значений кортеж состоящий из 2-х элементов – имя(str),
# возраст(int).  Сделать около 5-6 элементов словаря.
# Записать данный словарь на диск в json-файл.


import json

b_dict = {
          '159612': ('Tom', 23),
          '310640': ('Noah', 32),
          '044208': ('Jacob', 41),
          '233648': ('Liam', 21),
          '053872': ('Michael', 27),
          '403600': ('Anderson', 54)
}

with open('name_two.json', 'w') as f:
    json.dump(b_dict, f)
with open('name_two.json') as f:
    print(f.read())