konki = []
people = []
num_konki = int(input('Кол-во коньков: '))
num_people = int(input('Кол-во людей: '))
for i in range(1, num_konki+1):
    konki.append(int(input(f'Размер {i}-й пары: ')))
for i in range(1, num_people+1):
    people.append(int(input(f'Размер ноги {i}-го человека: ')))


temp = 0
for i in range(len(people)):
    if people[i] in konki:
        temp += 1
        konki.remove(people[i])


print(f'Наибольшее кол-во людей, которые могут взять ролики: {temp}')