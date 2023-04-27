import random 
#изменения
def search_number():



    while True :
        player1 = int(random.randint(1,5))
        player2 = int(input('угадай число от 1 до 5 '))
        answer = player1 - player2
        if player1 == player2 :
            print('угадал удача на твоей стороне')
            yes_or_no = input('хотите ли вы продолжить ')
        else:
            print(f'не угадал тебе не хватило {answer} попробуй еще раз мало ли в следующий раз провезет')
            yes_or_no = input('хотите ли вы продолжить ')
        if yes_or_no == 'нет':
            break
if __name__ == '__main__' :
    search_number()
//валера олух


