import game_search_number,dice.paradice
print('наш католог:','угадай число','стань ближе к нужному','дота пикер')
game = input('выбери игру которую хочешь погеймить')
if game == 'угадай число':
    game_search_number.search_number()
if game == 'стань ближе к нужному':
    dice.paradice.dice()






