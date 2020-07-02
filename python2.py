num= int(input('What is your favorite whole number?: '))

if (num % 2 == 0):
    print("Your favorite number is even!")
else:
    print("Your favorite number is odd")
if (num % 4 == 0):
    print("Did you know your number is a multiple of 4?")

num1= int(input('Give me a number: '))
num2= int(input('Give me one more: '))

if (num1 % num2 == 0):
    print('Did you know your numbers evenly divide into each other?')
else:
    print('Your numbers dont divide into each other')