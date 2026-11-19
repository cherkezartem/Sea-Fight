from .settings import * 
from .ships import * 
from .draw import * 
from .find_index import * 

# miss
def miss_shot(cur_cells, index_x, index_y, cor_x, cor_y, field_x):
    cur_cells[index_y][index_x] = "-"
    draw_miss(cor_x + SIZE / 2, cor_y - SIZE / 2)
    cross_out_field(field_x, SIZE*5)
    if player_turn[0] == 0:
        player_turn[0] = 1
    else:
        player_turn[0] = 0

# точки вокруг убитого корабля
def mark_around(cur_cells, field_x):
    for defeted_x, defeted_y in list_plus:
        for around_x, around_y in find_index_around(defeted_x, defeted_y):
            if 0 <= around_x <= 9 and 0 <= around_y <= 9:
                if cur_cells[around_y][around_x] == "x":
                    cur_cells[around_y][around_x] = "*"
                    around_cor_x = around_x * SIZE + field_x
                    around_cor_y = around_y * -SIZE + N//2 * SIZE
                    draw_around_destroyed(around_cor_x, around_cor_y)

# Проверка победы.
def check_win(cur_cells):
    for row in cur_cells:
        for elem in row:
            if elem in [4, 3, 2, 1]:
                return False
    return True

# Отрисовка всех попаданий на поле.
def draw_all_hits(cells, begin_x, begin_y):
    start_x = begin_x
    start_y = begin_y
    for row in cells:
        for elem in row:
            if elem == "+":
                draw_hit(start_x, start_y)
            start_x += SIZE
        start_y -= SIZE
        start_x = begin_x

# Показ кораблей в конце игры.
def show_ships():
    for ship in ships:
        ship.x -= 6 * SIZE
        ship.draw()
    for ship in ships_p2:
        ship.x += 6 * SIZE
        ship.draw()
    draw_all_hits(cells_p1, -11 * SIZE, 5 * SIZE)
    draw_all_hits(cells_p2, SIZE, 5 * SIZE)
    clear_cross()

# Клик по полю во время боя.
def fight_click(x: float, y: float):
    cur_cells = cells_p1
    if player_turn[0] == 0:
        field_x = (-N - 1) * SIZE
    else:
        cur_cells = cells_p2
        field_x = SIZE

    index_x = int((x - field_x) // SIZE)
    index_y = int((y - SIZE*(N/2)) // -SIZE)

    if 0 <= index_x <= 9 and 0 <= index_y <= 9:
        cor_x = index_x * SIZE + field_x
        cor_y = index_y * -SIZE + N//2 * SIZE
        if cur_cells[index_y][index_x] in ["n", "x"]:
            miss_shot(cur_cells, index_x, index_y, cor_x, cor_y, field_x)
        elif cur_cells[index_y][index_x] in ["-", "+", "*"]:
            return
        else:
            cur_cells[index_y][index_x] = "+"
            draw_hit(cor_x, cor_y)
            list_plus.clear()
            list_plus.append([index_x, index_y])
            if not check_ship_alive(cur_cells, index_x, index_y):
                mark_around(cur_cells, field_x)
                if check_win(cur_cells):
                    show_ships()
                    draw_text_win(player_turn[0])
    turn_arrow()
    screen.update()