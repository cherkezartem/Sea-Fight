from .settings import * 

def find_index_around(index_x, index_y):
    return [
        [index_x + 1, index_y],
        [index_x + 1, index_y - 1],
        [index_x + 1, index_y + 1],
        [index_x - 1, index_y],
        [index_x - 1, index_y - 1],
        [index_x - 1, index_y + 1],
        [index_x, index_y - 1],
        [index_x, index_y + 1],
    ]


def check_ship_alive(matrix, index_x, index_y, old_x=None, old_y=None):
    list_indexs = find_index_around(index_x, index_y)
    for around_x, around_y in list_indexs:
        if 0 <= around_x <= 9 and 0 <= around_y <= 9 and not (around_x == old_x and around_y == old_y):
            if matrix[around_y][around_x] in [4, 3, 2, 1]:
                return True
            elif matrix[around_y][around_x] == "+":
                list_plus.append([around_x, around_y])
                result = check_ship_alive(matrix, around_x, around_y, index_x, index_y)
                if result == True:
                    return True
    return False



def find_list_index(index_x, index_y, rotation, size):
    list_index = []
    for num in range(size):
        if rotation == 0:
            list_index.append([index_x + num, index_y])
        elif rotation == 90:
            list_index.append([index_x, index_y - num])
        elif rotation == 180:
            list_index.append([index_x - num, index_y])
        elif rotation == 270:
            list_index.append([index_x, index_y + num])
    return list_index