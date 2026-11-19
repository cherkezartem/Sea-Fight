import turtle
from .settings import * 
# Фнукция для создания квадратика.
def draw_square():
    for i in range(4):
        p_field.forward(SIZE)
        p_field.left(90)

# Функция для текста
def text(color_text: str, name: str):
    # Черепашка для текста.
    p_text.clear()
    p_text.hideturtle()
    p_text.color(color_text)
    p_text.pensize(5)
    p_text.penup()
    p_text.goto(0, 300)
    p_text.pendown()
    p_text.write(f"Розтошування {name} гравця ", align="center", font=(None, 30))


# Функция для создания поля.
def draw_field(x: int, y: int, n: int):
    for row in range(10):
        for col in range(10):
            p_field.penup()
            p_field.goto(x + col * SIZE, y + row * SIZE)
            p_field.pendown()
            draw_square()