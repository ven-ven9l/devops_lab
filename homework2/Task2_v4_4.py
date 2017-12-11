# Перепись
# https://acmp.ru/index.asp?main=task&id_task=131

m = 0
res = 0
for i in range(int(input("Enter N: "))):
    j = str((i + 1))
    s = input(j + " Enter V and S: ")
    l = s.split()
    g = int(l[0])
    if l[1] == '1':
        if g > m:
            m = g
            res = (i + 1)
print(res)
