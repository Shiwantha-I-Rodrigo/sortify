from random import randint


def bubblesort(num_list):
    for z in range(1, len(num_list) - 1):
        biggest_index = 0
        for i in range(0, len(num_list) - z):
            x = num_list[i]
            y = num_list[biggest_index]
            if y < x:
                biggest_index = i
        a = num_list[len(num_list) - z]
        b = num_list[biggest_index]
        num_list[len(num_list) - z] = b
        num_list[biggest_index] = a
        print(num_list)


listx = [randint(0, 99) for i in range(0, 10)]
print(listx)
print()
bubblesort(listx)