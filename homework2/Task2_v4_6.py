# Маска подсетей
# https://acmp.ru/index.asp?main=task&id_task=67

n_mask = 3
mask = ['255.255.255.0', '255.255.255.255', '255.255.255.0']
pairs = ['192.168.31.17 192.168.31.2', '192.168.31.3 192.168.31.4', '192.168.31.1 192.167.31.2']
n_pairs = 3
byte_mask = []
byte_pairs = []


def to_bytes(numb):
    code = ''
    numb = int(numb)
    for ind in range(8):
        if numb % 2 == 1:
            code += '1'
        else:
            code += '0'
        numb = int(numb / 2)
    return code


for i in range(n_mask):
    spl = mask[i].split('.')
    byte_mask.append('')
    for j in range(4):
        byte_mask[i] += to_bytes(spl[j])

for i in range(n_pairs):
    pairs[i] = pairs[i].split()
    byte_pairs.append([])
    for j in range(2):
        spl = pairs[i][j].split('.')
        byte_pairs[i].append('')
        for k in range(4):
            byte_pairs[i][j] += to_bytes(spl[k])
print("Masks: ", mask)
print("Byte masks: ", byte_mask)
print("Pairs: ", pairs)
print("Byte pairs: ", byte_pairs)

res = []
for i in range(n_pairs):
    res.append(0)
    for j in range(n_mask):
        n = 0
        f = 1
        for k in byte_mask[j]:
            if (k == '1') & (byte_pairs[i][0][n] != byte_pairs[i][1][n]):
                f = 0
                break
            n += 1
        res[i] += f
print("Result: ", res)
