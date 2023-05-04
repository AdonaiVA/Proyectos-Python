import random, math

class Player:
    def __init__(self,coins):
        self.coins = coins


def play(symbol):
    print ('-'*30)
    print('Welcom to Chardos Machine\n each game cost 2 coins')
    print ('-'*30)
    jugar = int(input('Do you want play?\n 1)YES\n 2)NO\n select a number:'))
    if jugar == 1:
        result = random.choices(symbol, k=3)
        print(f'|{result}|')
        if result[1] == result[2] and result[1] == result[0]:
            print('Jackpot! 💰')
        else:
            print('Thanks for playing!')
    else:
        print('Thanks for your time')
    return


print ('-'*30)

new_player = Player(10)

print(vars(new_player))

s = [' 🍒 ',' 🍇 ', ' 🍉 ', ' 7️⃣ ']


for i in range(5):
    play(s) 
    i += 1
    if i == 5:
        print('not enought coins :C')

    




