from modules import *

draw_field(int(-N/2 * SIZE), int(-N/2 * SIZE), 10)
text("red", "червоного")

for ship in ships:
    ship.draw()
    
screen.onclick(click)
screen.update()
screen.mainloop()