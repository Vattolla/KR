def func1(jd):
    a = 2400000 + jd + 32044
    b = int((4 * a + 3) / 146097)
    c = a - int((146097 * b) / 4)
    d = int((4 * c + 3) / 1461)
    e = c - int((1461 * d) / 4)
    m = int((5 * e + 2) / 153)
    drob = (float(jd) - int(float(jd)))

    date = int(e - int((153 * m + 2) / 5) + 1)
    month = m + 3 - 12 * int(m / 10)
    year = 100 * b + d - 4800 + int(m / 10)
    hour = 12 + drob * 24
    minute = (hour - int(hour)) * 60
    second = (minute - int(minute)) * 60

    hour_true = int(float(hour))                # Итоговые часы
    if hour_true >= 24:                         # Поправка, когда часов больше 24
        hour_true = hour_true - 24
        date = date + 1
    minute_true = int(float(minute))            # Итоговые минуты
    second_true = round((second), 2)            # Итоговые секунды

    gd = (f"{year}.{month}.{date}/ {hour_true}:{minute_true}:{second_true}")
    return gd


f11 = open("task2_data_easy.dat", 'r')
f1 = f11.readlines()
lines_of_f = len(f1)                            # Количество строк
v = 0
new_si = []
finally_list = []
print('Количество строк в таблице - ', lines_of_f)
name = input('Введите имя звезды ')
filter_star = input('Введите фильтр ')
print('-'*20)

for i in range(lines_of_f):
    si = f1[i].split()                          # Деление каждой строки на элементы
    if name.lower() == si[0].lower():
        if filter_star.lower() == si[2].lower():
            v += 1
            gd1 = func1(float(si[1]))
            new_si = [si[1], gd1, si[2], si[3]]
            finally_list.append(new_si)         # Запись всех новых строк в один список для дальнейшей сортировки)
finally_list.sort(key=lambda x: x[1])           # Спросить подробнее на счет ключей
print('Количество результатов -', v)
f11.close()

f2 = open(f'{name} {filter_star}', 'w')
for f_li in finally_list:
    fi = f2.write(str(f_li) + '\n')
f2.close()



            #print(new_si)
            #ansmans.append(new_si)
#ansmans.sort(key=lambda x: x[1])
#print(ansmans)
#for ans in ansmans:
   # print(ans)
            # fur = (float(si[1]) - int(float(si[1])))
            # print(round(fur, 4))
            # new_si.append(func1(si[1]))

#for j in si[0]:
    #if j.isalpha():
        #ns = ns + j.lower()
