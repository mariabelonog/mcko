f = open('vacancy.csv', encoding='utf-8').readlines()[1:]
f1 = [i.strip().split(';') for i in f]
d = {}
for i in f1:
    if i[-1].strip() in d.keys():
        d[i[-1].strip()].append([i[-2], i[0], i[1]])
    else:
        d[i[-1].strip()] = [[i[-2], i[0], i[1]]]

m = 0
k = 0
for i in d.keys():
    if len(d[i]) > m:
        k = i
        m = len(d[i])
print(k)