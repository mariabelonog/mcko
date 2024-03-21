f = open('vacancy.csv', encoding='utf-8').readlines()[1:]
f_out = open('vacancy_new.csv', 'w', encoding='utf-8')
f1 = [i.strip().split(';') for i in f]
f1.sort(key=lambda x: int(x[0]))
f_out.write(' - '.join(['company', 'Role', 'salary']) + '\n')
for i in f1[-3:]:
    f_out.write(' - '.join([i[4], i[3], i[0]]) + '\n')
