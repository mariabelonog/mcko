f = open('vacancy.csv', encoding='utf-8').readlines()[1:]
f1 = [i.strip().split(';') for i in f]


def sortted(s):
    for i in range(1, len(s)):
        key = s[i]
        j = i - 1
        while j >= 0 and key < s[j]:
            s[j + 1] = s[j]
            j -= 1
        s[j + 1] = s[i]


f1_sor = sorted(f1, key=lambda x: int(x[2]))
f1_new = list(filter(lambda x: x[3].strip().lower() == 'классный руководитель', f1_sor))
a = f1_new[0]
print(f'В компании {a[-1]} есть заданная профессия: {a[-2]}, з/п в такой компании составит: {a[0]}')