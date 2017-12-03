# Годовой баланс
# https://acmp.ru/index.asp?main=task&id_task=32

a = []
b = []
a.append(input("Input a: "))
b.append(input("Input b: "))
list_a = list(a[0])
list_b = list(b[0])
a[0] = int(a[0])
b[0] = int(b[0])
list_a.reverse()
list_b.reverse()
if a[0] < 0:
    list_a.pop()
    list_a.insert(0, '-')
if b[0] < 0:
    list_b.pop()
    list_b.insert(0, '-')
if a[0] % 10 != 0:
    a.append(int("".join(list_a)))
if b[0] % 10 != 0:
    b.append(int("".join(list_b)))
res = []
for i in range(len(a)):
    for j in range(len(b)):
        res.append(a[i] - b[j])
print("Max result: ", max(res))
