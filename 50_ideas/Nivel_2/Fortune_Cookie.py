import random



def fortune(i):
    if i == 1:
        print('Dont pursue happiness – create it.')
    elif i == 2:
        print('All things are difficult before they are easy.')
    elif i == 3:
        print('The early bird gets the worm, but the second mouse gets the cheese.')
    elif i == 4:
        print('If you eat something and nobody sees you eat it, it has no calories.')
    elif i == 5:
        print('Someone in your life needs a letter from you.')
    elif i == 6:
        print('Dont just think. Act!')
    elif i == 7:
        print('Your heart will skip a beat.')
    elif i == 8:
        print('The fortune you search for is in another cookie.')
    elif i == 9:
        print('Help! Im being held prisoner in a Chinese bakery!')
    
    return


i = int(input('Do you want me to read your fortune?\n 1)Yes\n 2)No\n Select a number: '))

if i == 1:
    x = random.randint(1,9)
    fortune(x)

else:
    print('See you later')


    
