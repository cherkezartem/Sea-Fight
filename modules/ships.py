import turtle
from .draw import draw_button
from .settings import *


class Ship():
    def __init__(self, x: int, y: int,color: str, selected_color: str, size: int):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.selected_color = selected_color
        self.rotate = 270
        self.paint = turtle.Turtle()
        self.paint.hideturtle()
        self.paint.pensize(1)
        self.paint.speed(0)
        self.save = False
        self.start_x = x
        self.start_y = y
    def draw(self):
        self.paint.clear()
        self.paint.setheading(0)
        self.paint.penup()
        if self == selected_ship[0]:
            draw_button(300, -190)  
            self.paint.color(self.selected_color)
        else:
            self.paint.color(self.color)
        for num in range(self.size):
            self.paint.penup()
            if self.rotate == 0:
                self.paint.goto(self.x + SIZE*num, self.y)
            elif self.rotate == 90:
                self.paint.goto(self.x , self.y + SIZE*num)
            elif self.rotate == 180:
                self.paint.goto(self.x - SIZE*num, self.y)
            elif self.rotate == 270:
                self.paint.goto(self.x , self.y - SIZE*num)
            self.paint.pendown()
            self.paint.begin_fill()
            for i in range(4):
                self.paint.forward(SIZE)
                self.paint.right(90)
            self.paint.end_fill()

# Список кораблей.
ships = [
    Ship(300, 250, "orange", "#f9b062", 4),
    Ship(375, 250, "green","#61ff56", 3),
    Ship(375, 75, "green","#61ff56", 3),
    Ship(450, 250, "blue", "#56e6ff", 2),
    Ship(450, 125, "blue","#56e6ff", 2),
    Ship(450, 0, "blue","#56e6ff", 2),
    Ship(525, 250, "purple","#ff56f9", 1),
    Ship(525, 175, "purple","#ff56f9", 1),
    Ship(525, 100, "purple","#ff56f9", 1),
    Ship(525, 25, "purple","#ff56f9", 1)
]
ships_p2 = [
    Ship(300, 250, "orange", "#f9b062", 4),
    Ship(375, 250, "green","#61ff56", 3),
    Ship(375, 75, "green","#61ff56", 3),
    Ship(450, 250, "blue", "#56e6ff", 2),
    Ship(450, 125, "blue","#56e6ff", 2),
    Ship(450, 0, "blue","#56e6ff", 2),
    Ship(525, 250, "purple","#ff56f9", 1),
    Ship(525, 175, "purple","#ff56f9", 1),
    Ship(525, 100, "purple","#ff56f9", 1),
    Ship(525, 25, "purple","#ff56f9", 1)
]



# Матрица поля.
cells_p1 = []
for i in range(10):
    cells_p1.append([])
    for n in range(10):
        cells_p1[-1].append("n")
cells_p2 = []
for i in range(10):
    cells_p2.append([])
    for n in range(10):
        cells_p2[-1].append("n")