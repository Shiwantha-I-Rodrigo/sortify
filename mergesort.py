from random import randint


def merge(listL, listR):
    listX = []

    if len(listL) >= len(listR):
        for R in listR:
            if listL:
                while (R >= listL[0]):
                    listX.append(listL.pop(0))
                    if not listL:
                        break
            listX.append(R)

        if listL:
            for L in listL:
                listX.append(L)

    print(listX)



listx = [randint(0, 9) for i in range(0, 5)]
listy = [randint(0, 9) for i in range(0, 5)]
listx.sort()
listy.sort()
print(listx, listy)
merge(listx, listy)

