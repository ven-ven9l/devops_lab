# Most Common
# https://www.hackerrank.com/challenges/most-commons/problem
s = "iiiiiiiiiiisdfasdfasdfvsaeeeeeeendsynfgzssbdfmdfbsaaaadvrzgrbszvseaeoooofa.dsvqbaetbawabcdefghilkjj"
d = {}
k = 0
for i in list(s):
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
d = sorted(d.items(), key=lambda x: (-x[1], x[0]))
for i in range(3):
    print(str(d[i][0]) + " " + str(d[i][1]))