import time#импортируем нужную встроенную библиотеку
#time = time.time()#первый метод. Он показывает сколько времени прошло с начала эпохи а то есть с хер знает какого года. Служит  самой главной функцией т к передается в качестве аргумента много где
#print(time)

print(time.asctime())#выводит день недели месяц число час минуту секунду и год в момент запуска программы. ВСЕ ЭТО БЕРЕТСЯ ИММЕНО С КОМПЬЮТЕРА А НЕ ЛОКАЛЬНО

#for i in range(1,60):#Создаем цикл на 60 итераций
#    print(i)#выводим нынешнюю итерацию
#    time.sleep(1)#еще один метод. приостанавливает программу на указанное число. Таким образом можно создать таймер на минуту или отсчет на час

result = time.localtime(time.time())# выводит кортеж с теми же данными только в немного другом формате. ИСПОЛЬЗОВАТЬ ТОЛЬКО ЭТОТ МЕТОД ТК БЕРЕТСЯ ЛОКАЛЬНОЕ ЗНАЧЕНИЕ А НЕ ЗНАЧЕНИЕ С КОМПА
print(result)#
print(result.tm_mday)#тк данные выводятся именно как кортеж можно запросить конкретный элемент этого самого кортежа


print(time.gmtime(time.time()))#НЕНУЖНО. выводит все то же самое только по всемирному времени UTC

time_str = time.strftime("%m.%d.20%y %H:%M:%S")#может вывести что то конкретное в формате строки
print(time_str)#

time_str = "11 June, 2025"#
print(time.strptime(time_str,"%d %B, %Y"))#передаем строку а потом этот метод переводит ее в кортеж в привычном для него формате