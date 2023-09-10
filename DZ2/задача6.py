list1 = []
list2 = []

for i in range(1,4):
    list1.append(int(input(f'Введите {i}-е число: ')))
for i in range(1,8):
    list2.append(int(input(f'Введите {i}-е число: ')))
print(f"Новый первый список с уникальными элементами: {list(set(list1+list2))}")
