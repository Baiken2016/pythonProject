guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

temp = True
while temp:
    ans = input('гость пришел или ушел? ')
    guest = (input('имя гостя: '))
    print(guests)
    if ans == 'пришел' and len(guests)!=6:
        print(f'Привет {guest}!')
        guests.append(guest)
        print(guests)
    elif ans == 'пришел' and len(guests)==6:
        print(f'извини {guest}')
        temp = False
        break
    elif ans == 'ушел':
        print(f'пока {guest}')
        guests.remove(guest)
        print(guests)

