num = int(input('Кол-во человек: '))
people_list = []
for i in range(1,num+1):
    people_list.append(i)

while len(people_list)!=1:
    num2 = int(input('Какое число в считалке?: '))
    print(f"Значит выбывает каждый {num2}-й человек")
    num3 = int(input('Начало счета с номера: '))
    if num2>len(people_list):
        while num2>len(people_list):
            num2 = num2%len(people_list)
    else:
print(23)    ваукп