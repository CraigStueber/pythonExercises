num = int(input("Give me a whole number:"))
listRange = list(range(1, num+1))
divList=[]
for element in listRange:
    if (num % element == 0):
        divList.append(element)
print(divList)