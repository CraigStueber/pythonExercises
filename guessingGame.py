import random


num = random.randint(1,100)
pick = 0
count = 0
print('I am thinking of a number between 1 and 100. Can you guess it?\nType exit to quit')
while (pick != num and pick != 'exit'):
    pick = input('Pick a number:\n')
    
    if (pick == 'exit'):
        break
    pick= int(pick)
    count += 1

    if (pick < num):
        print('To low')
    elif (pick > num):
        print('To high')
    else:
        print('You got it right!')
        break

