### 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
#Примеры:

#duration = 53
#53 сек
#duration = 153
#2 мин 33 сек
#duration = 4153
#1 час 9 мин 13 сек
#duration = 400153
#4 дн 15 час 9 мин 13 сек

#duration = int(input('Введите время в секундах: '))
#days = duration // (60 * 60 * 24)
#hours = (duration - days * (60 * 60 * 24) // (60 * 60))
#min = (duration - days * (60 * 60 * 24) - hours * (60 * 60)) // 60
#sec = (duration - days * (60 * 60 * 24) - hours * (60 * 60) - min * 60)
#print(days,'дни',hours,'час',min,'мин',sec,'сек')

#task2

#my_list = []
#for num in range (1, 1001, 2):
 #   my_list.append(num ** 3)
#a
#final_sum = 0
#for num in my_list:
#    check_sum = 0
#    for check_num in str(num):
#        check_sum += int(check_num)
#    if check_sum % 7 ==0:
#        final_sum += num
#print(final_sum)

#task 3

percent = int(input('Ввдите число процена: '))
if percent == 1:
  word = 'процент'
elif percent <= 4:
    word = 'процентов'
else:
    word = 'процентов'
print(percent, word)
