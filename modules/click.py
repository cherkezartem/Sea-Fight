from .settings import * 
from .ships import * 
from .draw import * 
from .find_index import * 
from .field import *
from .fight import * 

# Клик по клеточкам.
def cell_click(index_x, index_y, cur_cells, cur_ships):
    cor_x = index_x * SIZE - N//2 * SIZE
    cor_y = index_y * -SIZE + N//2 * SIZE
    if selected_ship[0] != None:
        list_index = find_list_index(index_x, index_y, selected_ship[0].rotate, selected_ship[0].size)
        end_index_x, end_index_y = list_index[-1]
        # размищение корабликов
        if 0 <= end_index_x <= 9 and 0 <= end_index_y <= 9:
            can_paste = True
            for paste_x, paste_y in list_index:
                if cur_cells[paste_y][paste_x] != "n":
                    can_paste = False
                    break
            if can_paste:
                selected_ship[0].x = cor_x
                selected_ship[0].y = cor_y
            
# Клик по корабликам.
def ship_click(x, y, cur_ships: list[Ship]):
    for ship in cur_ships:
        if ship.save == False:
            start_x = ship.x
            start_y = ship.y
            end_x = ship.x + SIZE
            end_y = ship.y - SIZE*ship.size
            if( x >= start_x and x <= end_x) or ( x <= start_x and x >= end_x):
                if( y >= start_y and y <= end_y) or ( y <= start_y and y >= end_y):
                    selected_ship[0] = ship

# Клик по кнопкам.
def button_click(x, y, cur_ships, cur_cells):
    global selected_ship
    reset_ship = True
    if y <= -190 and y >= -250 and selected_ship[0] != None:
        # reset but
        if x >= 300 and x <= 450:
            cur_ships [selected_ship[0]].x = selected_ship[0].start_x
            selected_ship[0].y = selected_ship[0].start_y
            selected_ship[0].rotate = 270
        # rotate but
        elif x >= 475 and x <= 625:
            rotate_index_x = int((selected_ship[0].x + SIZE*(N/2)) // SIZE)
            rotate_index_y = 10 -int((selected_ship[0].y + SIZE*(N/2)) // SIZE)
            new_rotate = selected_ship[0].rotate + 90
            if new_rotate >= 360:
                new_rotate = 0
            if not (0 <= rotate_index_x <= 9 and 0 <= rotate_index_y <= 9):
                selected_ship[0].rotate = new_rotate
                reset_ship = False
            else:
                list_index = find_list_index(rotate_index_x, rotate_index_y, new_rotate, selected_ship[0].size)
                end_index_x, end_index_y = list_index[-1]
                if 0 <= end_index_x <= 9 and 0 <= end_index_y <= 9:
                    can_paste = True
                    for paste_x, paste_y in list_index:
                        if cur_cells[paste_y][paste_x] != "n":
                            can_paste = False
                            break
                    if can_paste:
                        selected_ship[0].rotate = new_rotate
                        reset_ship = False
        # save but
        elif x >= 650 and x <= 800:
            save_index_x = int((selected_ship[0].x + SIZE*(N/2)) // SIZE)
            save_index_y = 10 -int((selected_ship[0].y + SIZE*(N/2)) // SIZE)
            list_index = find_list_index(save_index_x, save_index_y, selected_ship[0].rotate, selected_ship[0].size)
            reset_ship = False
            for save_x, save_y in list_index:
                cur_cells[save_y][save_x] = selected_ship[0].size
                save_around_list = find_index_around(save_x, save_y)
                for around_x, around_y in save_around_list:
                    if 0 <= around_x <= 9 and 0 <= around_y <= 9:
                        if cur_cells[around_y][around_x] == "n":
                            cur_cells[around_y][around_x] = "x"
            selected_ship[0].save = True
            selected_ship[0] = None
    if reset_ship:
        if selected_ship[0] != None:
            # selected_ship[0].x = selected_ship[0].start_x
            selected_ship[0].x = selected_ship[0].start_x
            selected_ship[0].y = selected_ship[0].start_y
            selected_ship[0].rotate = 270
        selected_ship[0] = None
    
# Функция для клика.
def click(x: float, y: float):
    if game_phase[0] == "arrangement":
        cur_cells = cells_p1
        cur_ships = ships
        if player_turn[0] == 1:
            cur_ships = ships_p2
            cur_cells = cells_p2

        index_x = int((x + SIZE*(N/2)) // SIZE)
        index_y = int((y - SIZE*(N/2)) // -SIZE)
        if 0 <= index_x <= 9 and 0 <= index_y <= 9:
            cell_click(index_x, index_y, cur_cells, cur_ships)
        else:
            button_click(x, y, cur_ships, cur_cells)
        
        ship_click(x, y, cur_ships)
        change_turn = True
        for ship in cur_ships:
            if ship.save == False:
                change_turn = False
                break
        if change_turn == True:
            if player_turn[0] == 0:
                player_turn[0] = 1
                cur_ships = ships_p2
                text("#007BFF", "синього")
                for ship in ships:
                    ship.paint.clear()
            else:
                game_phase[0] = "fight"
                for ship in ships_p2:
                    ship.paint.clear()
                p_field.clear()
                draw_field(int((-N - 1) * SIZE), int(-N/2 * SIZE), 10)
                draw_field(SIZE, int(-N/2 * SIZE), 10)
                cross_out_field(int((-N - 1) * SIZE), int(N/2 * SIZE))
                p_text.clear()
                p_text.penup()
                p_text.goto(int((-N - 1) * SIZE), int(N/2 * SIZE))
                p_text.pendown()
                p_text.color("red")
                p_text.write("Поле червоного", font=(None, 30))
                p_text.penup()
                p_text.goto(SIZE, int(N/2 * SIZE))
                p_text.pendown()
                p_text.color("#007BFF")
                p_text.write("Поле синього", font=(None, 30))
                turn_arrow()
        if game_phase[0] == "arrangement":
            for ship in cur_ships:
                ship.draw()

        if selected_ship[0] is None:
            clear_but()
        screen.update()
    
    elif game_phase[0] == "fight":
        fight_click(x, y)

    screen.update()

