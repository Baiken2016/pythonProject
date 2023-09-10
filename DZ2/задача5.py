violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

song_dict = {}
for i in violator_songs:
    if i[0] not in song_dict:
        song_dict[i[0]] = i[1]
    else:
        song_dict[i[0]] += i[1]
temp = True
song_len = 0
while temp:
    num = int(input('Сколько песен выбрать? '))
    if num <= len(song_dict):
        for i in range(1,num+1):
            song_name = input(f'Название {i}-й песни: ')
            if song_name in song_dict:
                song_len += song_dict.get(song_name)
            else:
                continue
        print(f'Общее время звучания песен: {round(song_len, 2)}')
    else:
        temp = False
        print('ошибка')
        break