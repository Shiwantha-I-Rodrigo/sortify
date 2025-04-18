from random import randint


def bubblesort(num_list):
    for z in range(1, len(num_list) - 1):
        for i in range(0, len(num_list) - z):
            x = num_list[i]
            y = num_list[i+1]
            if y < x:
                num_list[i]=y
                num_list[i+1]=x
            print(num_list)


listx = [randint(0, 99) for i in range(0, 20)]
print(listx)
print()
bubblesort(listx)