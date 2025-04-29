from random import randint


def insertionsort(num_list):
    for z in range(1, len(num_list)):
        active_index = insert_position = z
        for i in range(z-1, -1, -1):
            x = num_list[i]
            y = num_list[active_index]
            if y < x:
                insert_position = i
        num_list.pop(active_index)
        num_list.insert(insert_position,y)
        print(f"move {y} from {active_index} to {insert_position}")
        print(num_list)


listx = [randint(0, 9) for i in range(0, 10)]
print(listx)
insertionsort(listx)