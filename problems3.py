company = input()
f = open('vacancy.csv', encoding='utf-8').readlines()[1:]
f1 = [i.strip().split(';') for i in f]
while company != 'None':
    for i in f1:
        if i[4] == company:
            print(f'В {company} найдена вакансия: <вакансия>. З/п составит: {i[0]}')
    company = input()