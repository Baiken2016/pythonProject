shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
shop_dict = {}
for i in shop:
    if i[0] not in shop_dict:
        shop_dict[i[0]] = [i[1],1]
    else:
        shop_dict[i[0]][0]+=i[1]
        shop_dict[i[0]][1]+=1
print(shop_dict)
temp = True
while temp:
    ans = input('Введите название детали: ')
    if ans in shop_dict.keys():
        print(f"""Название детали: {ans}
Кол-во деталей: {shop_dict.get(ans)[1]}
Общая стоимость: {shop_dict.get(ans)[0]}""")
    else:
        print('детали нет')
        temp = False
        
