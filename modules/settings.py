import turtle

turtle.hideturtle()
# Экран.
screen = turtle.Screen()
screen.setup(1920, 1080)
screen.bgcolor("#393939")
screen.title("Морський бій")
screen.tracer(0, 0)

# Черепашка для кнопок.
paint_button = turtle.Turtle()
paint_button.hideturtle()
paint_button.pensize(5)
paint_button.speed(0)
paint_button.color("#ffffff")

# Черепашка для поля.
p_field = turtle.Turtle()
p_field.hideturtle()
p_field.pensize(5)
p_field.speed(0)
p_field.color("#ffffff")

# Черепашка для хода.
p_turn = turtle.Turtle()
p_turn.hideturtle()
p_turn.pensize(5)
p_turn.speed(0)
p_turn.color("#ffffff")

# Черепашка для стрелочки.
p_arrow = turtle.Turtle()
p_arrow.hideturtle()
p_arrow.pensize(5)
p_arrow.speed(0)

# Черепашка для зачеркивания поля.
p_cross_field = turtle.Turtle()
p_cross_field.hideturtle()
p_cross_field.pensize(2)
p_cross_field.speed(0)
p_cross_field.color("#ADA7A7")

# Черепашка для текста.
p_text = turtle.Turtle()
p_text.hideturtle()

# Выбранный кораблик, константы.
selected_ship = [None]
player_turn = [0]
list_plus = []
SIZE_BUTTON = 100
SIZE = 50
N = 10
game_phase = ["menu"]
mode_play = [None]
