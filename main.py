from ursina import *
import random
from random import uniform


app = Ursina()
score = 0
missed = 0

class Background(Button):
    def __init__(self):
        super().__init__(
            model="quad",
            parent=scene,
            color=color.gray,
            scale=25,
        )

    def on_click(self):
        global missed
        missed = missed + 1
        self.color=color.gray

    def on_mouse_enter(self):
        pass  

    def on_mouse_exit(self):
        pass
    



class Box(Button):
    def __init__(self):
        super().__init__(
            model="circle",
            parent=camera.ui,
            color=color.green,
            scale=0.035,
            position=(0, 0)
        )

    def on_click(self):
        global score
        score = score + 1
        self.position = (uniform(-.86, .86), uniform(-.47, .47))

    def on_mouse_exit(self):
        self.color = color.white

bg = Background()
box = Box()

def display_results():
    window_panel = WindowPanel(
        title=f"Game Over\nTotal Score: {score}\nTotal Missed: {missed}",
        content=f"Total Missed: {missed}\nTotal Score: {score}",
        model="quad",
        scale=(0.5, 0.3),
        background=True,
        background_color=color.white66,
        text_origin=(-0.2, 0.05),
        text_scale=1.5,
    )

    def close_panel():
        window_panel.close()
        application.quit()  

    invoke(close_panel, delay=2) 

def input(key):
    if key == 'escape':
        display_results()

app.run()
