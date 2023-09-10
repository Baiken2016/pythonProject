a = [1,5,3]
b = [1,5,1,5]
c = [1,3,1,5,3,3]
a += b

temp = 0
for i in a:
    if i == 5:
        temp +=1
print(temp)
print(a)
for i in enumerate(a):
    if i[1] == 5:
        a.pop(i[0])

a += c
temp1 = 0
for i in a:
    if i==3:
        temp1+=1
print(temp1)
print(a)
