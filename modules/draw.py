from .settings import *

# Стирание кнопок.
def clear_but():
    paint_button.clear()

# Отрисовка кнопок
def draw_button(start_but_x: int, start_but_y: int):
    paint_button.clear()
    text_list = ["Відхилити", "Повернути", "Зберегти"]
    for x_changer in range(3):
        paint_button.penup()    
        paint_button.goto(start_but_x + x_changer*175, start_but_y)
        paint_button.pendown()
        for i in range(4):
            if i %2 == 0:
                paint_button.forward(150)
            else:
                paint_button.forward(60)
            paint_button.right(90)
        paint_button.penup()
        paint_button.goto(start_but_x + x_changer*175 + 75, start_but_y - 40)
        paint_button.pendown()
        paint_button.write(text_list[x_changer], align="center", font=(None, 22))


# Функция отрисовки кораблей.


def draw_miss(x, y):
    p_turn.penup()
    p_turn.goto(x, y)
    p_turn.pendown()
    p_turn.color("#007BFF")
    p_turn.dot(15)

def draw_hit(x, y):
    p_turn.color("#FF0000")
    p_turn.penup()
    p_turn.goto(x + SIZE / 4, y - SIZE / 4)
    p_turn.pendown()
    p_turn.goto(x + SIZE - SIZE / 4, y - SIZE + SIZE / 4)
    p_turn.penup()
    p_turn.goto(x + SIZE - SIZE / 4, y - SIZE / 4)
    p_turn.pendown()
    p_turn.goto(x + SIZE / 4, y - SIZE + SIZE / 4)

def draw_around_destroyed(x, y):
    p_turn.color("#007BFF")
    p_turn.penup()
    p_turn.goto(x + SIZE / 3, y - SIZE / 3)
    p_turn.pendown()
    p_turn.goto(x + SIZE - SIZE / 3, y - SIZE + SIZE / 3)
    p_turn.penup()
    p_turn.goto(x + SIZE - SIZE / 3, y - SIZE / 3)
    p_turn.pendown()
    p_turn.goto(x + SIZE / 3, y - SIZE + SIZE / 3)

def cross_out_field(start_x, start_y):
    p_cross_field.clear()
    for num in range(0, 10*SIZE, 25):
        p_cross_field.penup()
        p_cross_field.goto(start_x + num, start_y)
        p_cross_field.pendown()
        p_cross_field.goto(start_x, start_y - num )
    for num in range(0, 10*SIZE, 25):
        p_cross_field.penup()
        p_cross_field.goto(start_x + num, start_y - 10 * SIZE)
        p_cross_field.pendown()
        p_cross_field.goto(start_x + 10 * SIZE, start_y - num )

def clear_cross():
    p_cross_field.clear()

def turn_arrow():
    p_arrow.clear()
    p_arrow.penup()
    p_arrow.goto(0, 0)
    p_arrow.pendown()
    if player_turn[0] == 1:
        p_arrow.color("red")
        p_arrow.setheading(0)
    else:
        p_arrow.color("#007BFF")
        p_arrow.setheading(180)   
    p_arrow.forward(30)       
    p_arrow.left(150)
    p_arrow.forward(20)       
    p_arrow.backward(20) 
    p_arrow.right(300)
    p_arrow.forward(20)
    
def draw_text_win(player: int):
    p_text.penup()
    p_text.goto(0, 375)
    p_text.pendown()
    text = "Переміг червоний гравець"
    if player == 0:
        p_text.color("red")
    else:
        p_text.color("#007BFF")
        text = "Переміг синій гравець"
    p_text.write(text, align="center", font=(None, 65))
