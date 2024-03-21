f = open('vacancy.csv', encoding='utf-8').readlines()[1:]
f_out = open('vacancy_procent.csv', 'w', encoding='utf-8')
f1 = [i.strip().split(';') for i in f]
d = {} #dictionary with the vacancy types and salaries
for i in f1:
    if i[1] not in d.keys():
        d[i[1].strip().lower()] = [int(i[0])]
    else:
        d[i[1]].append(int(i[0]))
d1 = {} #dictioanry with vacancies and averedge salary
for i in d.keys():
    d1[i] = round(sum(d[i]) / len(d[i]))


def percent(i):
    i.append(str(round(round(int(i[0]) / d1[i[1].strip().lower()], 2) * 100)))
    return i


f_out.write('Salary;Work_Type;Company_Size;Role;Company;Percent\n')
for i in f1:
    f_out.write(';'.join(percent(i)) + '\n')
