import random
def dice():



    number_which_need_to_hide = random.randint(1,100)
    player1 = int(input('игрок номер 1 введите число от 1 дт 100 '))
    player2 = int(input('игрок номер 2 введите число от 1 дт 100 '))
    something = [number_which_need_to_hide,player1,player2]
    something.sort()
    winner = something[1]
    s = winner
    if player1 == winner :
        print(' игрок под номером 1 оказался ближе ')
    if player2 == winner :
        print('игрок под номером 2 оказался ближе ')
    if number_which_need_to_hide == winner :
        a = player1 - winner
        b = player2 - s
        if abs(a) > abs(b) :
            print('игрок под номером 2 оказался ближе')
        if abs(a) < abs(b) :
            print('игрок под номером 1 оказался ближе')
    print(f'таблица{something}')



if __name__ == '__main__' :
    dice()


