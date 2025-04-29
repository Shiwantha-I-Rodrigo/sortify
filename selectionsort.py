from random import randint


def selectionsort(num_list):
    for z in range(1, len(num_list)):
        biggest_index = 0
        final_position = len(num_list) - z
        for i in range(0, final_position + 1):
            x = num_list[i]
            y = num_list[biggest_index]
            if y < x:
                biggest_index = i
        a = num_list[final_position]
        b = num_list[biggest_index]
        num_list[final_position] = b
        num_list[biggest_index] = a
        print(f"move {b} from {biggest_index} to {final_position}")
        print(num_list)


listx = [randint(0, 9) for i in range(0, 10)]
print(listx)
selectionsort(listx)