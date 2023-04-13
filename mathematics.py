from datetime import datetime
import time 
import random
start_time = datetime.now()
finish_time = datetime.now()
g = []
s = 0
while True:
    print(g)
    trust_back = int(random.randint(1,4))
    a = random.randint(1,10)
    b = random.randint(1,10)
    timing = finish_time - start_time
    if trust_back == 1 :
        s = a + b
        print(a,'+',b)
        player = input('введи их сумму ')
        if s == player:
            g.append(finish_time - start_time)
    if trust_back == 2 :
        s = a - b
        print(a,'-',b)
        player = input('введи их разность ')
        if s == player:
            g.append(finish_time - start_time)
    if trust_back == 3 :
        s = a * b
        print(a,'*',b)
        player = input('введи их произведение ')
        if s == player:
            g.append(finish_time - start_time)
    if trust_back == 4 :
        s = a / b
        print(a,'/',b)
        player = input('введи их частное ')
        if s == player:
            g.append(finish_time - start_time)
    if len(g) == 4:
        break


