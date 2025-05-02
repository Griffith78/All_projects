from threading import Thread#импорт многопоточности
import time#импорт модуля time

def one(num):#
    time.sleep(num)#функция которая задерживает программу на введеное время

def two(num):#
    time.sleep(num)#точно такая же функция

t1 = Thread(target = one, args = (1,))#создаем поток который будет выполнять функцию one а в аргумент будет передавать 1
t2 = Thread(target = two,args = (1,))#точно также

x1 = time.time()#возвращает текущее время

t1.start()#запускаем первый поток
t2.start()#запускаем второй поток

t1.join()#проверяем был ли завершен первый поток. Если же он не был завершен то основной поток программы не продолжит свою работу
t2.join()#точно также делаем со вторым потоком

x2 = time.time()#опять возвращает текущее время

#print(x2 - x1)#вычитаем время x1 из времени x2

def timer1(num = 60):
    for i in range(0,num):
        print(i)
        time.sleep(1)

def timer2(num = 60):
    for i in range(0,num):
        print(i)
        time.sleep(1)

#пример асинхронной задачи
t1 = Thread(target = timer1,args = ())
time1 = time.time()

t1.start()
time.sleep(1)
timer2()

t1.join()

time2 = time.time()

print(time2 - time1)