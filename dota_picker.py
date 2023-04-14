import random
import time
from datetime import datetime
import main
#==================================PICKER===================================================
heroes = []
def picker():
  print('===КОМАНДЫ===') 
  print('1. ДОБАВИТЬ ГЕРОЯ')
  print('2. PICK')
  print('3. ESC')
  command = int(input('Выберите команду: '))
  if command == 1:
    ap_heroes = input('Напиши героя, которого ты хочешь добавить в список')
    heroes.append(ap_heroes)
    picker()
  if command == 2:
    pik_rand = random.randint(0, len(heroes) - 1) 
    print(*heroes)
    print(*heroes[pik_rand])
    picker()
  if command == 3:
    main.game_choice()
    
if __name__ == '__main__':
    picker()
#===========================================================================================
