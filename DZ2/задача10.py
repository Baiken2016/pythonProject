num = int(input('кол-во чисел: '))
list1 = []
list2 = []
while len(list1)!=num:
    list1.append(int(input('Число: ')))
for i in list1[len(list1)-2::-1]:
    list2.append(i)
print(list1)
print(list2)