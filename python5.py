a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]

def overlap(val1, val2, val3):
    for i in val1:
        if i in val2:
            if i not in val3:
                val3.append(i)

overlap(a, b, c)
print(c)