from random import randint


def merge(listL, listR):
    print(f"merge {listL} and {listR}")
    listX = []

    if len(listR) >= len(listL):
        for L in listL:
            if listR:
                while (L >= listR[0]):
                    listX.append(listR.pop(0))
                    if not listR:
                        break
            listX.append(L)

        if listR:
            for R in listR:
                listX.append(R)

    return listX


def split(listT):
    print(f"split {listT}")
    if len(listT) <= 1:
        return listT

    mid = len(listT) // 2
    left = listT[:mid]
    right = listT[mid:]

    sortedLeft = split(left)
    sortedRight = split(right)

    return merge(sortedLeft, sortedRight)


listU = [randint(0, 99) for i in range(0, 20)]
print(listU)
print("<<<start>>>")
print(split(listU))