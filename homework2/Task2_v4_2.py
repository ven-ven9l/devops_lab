# Годовой баланс
# https://acmp.ru/index.asp?main=task&id_task=32
a = []
b = []
# a.append(input("Input a: "))
# b.append(input("Input b: "))
a.append('-10983')  # Debet
b.append('-12310')    # Kredit

list_a = list(a[0])
list_b = list(b[0])
a[0] = int(a[0])
b[0] = int(b[0])

if a[0] < 0:
    list_a = sorted(list_a)
    j = 1
    while list_a[j] == '0':
        j += 1
    if j >= 1:
        list_a[1], list_a[j] = list_a[j], list_a[1]
else:
    list_a = sorted(list_a, reverse=True)

if b[0] < 0:
    list_b = sorted(list_b, reverse=True)
    list_b.pop()
    list_b.insert(0, '-')
else:
    list_b = sorted(list_b)
    j = 0
    while list_b[j] == '0':
        j += 1
    if j >= 1:
        list_b[0], list_b[j] = list_b[j], list_b[0]

stra = ''
for i in list_a:
    stra += i
strb = ''
for i in list_b:
    strb += i

print("Debet: ",int(stra))
print("Kredit: ",int(strb))

print("Max result: ", (int(stra) - int(strb)))
