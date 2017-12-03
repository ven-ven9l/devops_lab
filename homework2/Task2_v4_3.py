# Hamming Distance
# https://leetcode.com/problems/hamming-distance/description/

x = int(input("Enter x: "))
y = int(input("Enter y: "))
d = 0
res = [0]
while (x > 0) | (y > 0):
    print(x % 2, y % 2)
    if (x % 2) != (y % 2):
        d += 1
    res.append(d)
    x = int(x / 2)
    y = int(y / 2)
print("Hamming distance:", max(res))
