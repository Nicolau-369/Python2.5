from datetime import date

data1 = date(2024, 4, 10)
print(date.today())

hoje = date.today()
data2 = date(hoje.year, hoje.month, 1)
print(data2)

oscar_2024 = date(2024, 2, 24)
tempo_para_o_oscar = abs(oscar_2024 - hoje)
print(tempo_para_o_oscar.days)

print(hoje.weekday())

data2 = data2.replace(day=3)
print(data2)

print(data2.strftime("%d/%m/%Y"))