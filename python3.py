a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x=[]
y=int(input('Please give me a whole number:'))
for element in a:
    if (element < y):
        x.append(element)
print(x)
