from datetime import datetime
import time 
import random
start_time = datetime.now()
g = []
s = 0
m = 0
print('отвечать неправильно и скипать нельзя')
while len(g) != 4:
    try:
        trust_back = int(random.randint(1,3))
        a = random.randint(1,10)
        b = random.randint(1,10)
        start_time = datetime.now()
        if trust_back == 1 :
            s = a + b
            print(a,'+',b)
            player = int(input('введи их сумму '))
        if trust_back == 2 :
            s = a - b
            print(a,'-',b)
            player = int(input('введи их разность '))
        if trust_back == 3 :
            s = a * b
            print(a,'*',b)
            player = int(input('введи их произведение '))
        finish_time = datetime.now()
        print(f'ты решил за {finish_time - start_time}')
        if s != player:
                print('но не верно')
                m += 1
        if s == player:
            timing = finish_time - start_time
            g.append(timing.seconds)
        if len(g) == 4:
            print(f'в среднем твой результат это {sum(g) / len(g) + m}')
    except:
        print('вы ввели не то,что я ждал')


