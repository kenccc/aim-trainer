from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import uniform
app = Ursina()
totalClicks = 0
score = 0
class Voxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube',
            color = color.white,
            highlight_color = color.lime,
         )
def display_results():
    window = WindowPanel(title=f"Score: {score}\n Missed: {totalClicks - score}")
    def close_panel():
        window.close()
        application.quit()

    invoke(close_panel, delay=2)

def input(key):
    print(key)
    if key == "escape" or key =="f4":
        display_results()
    if key == "left mouse down":
        global totalClicks
        totalClicks += 1

class Target(Button):
    def __init__(self , position = (12,2,12), scale = 0.7):
        super().__init__(
            parent=scene,
            position = position,
            model = "sphere",
            origin_y = 0.5,
            scale= scale,
            color= color.white,
            highlight_color = color.yellow,
        )
    def on_click(self):
        global score
        score += 1
        newX = uniform(5.5,16.5)
        newY = uniform(1, 2.8)
        self.position = (newX,newY)
        self.scale = uniform(0.3,0.7)
class WallX1(Entity):
    def __init__(self,position=(14.5,0,15)):
        super().__init__(
            parent = scene,
            model = "cube",
            scale = (30, 10, 5),
            position = position,
            color = color.gray,
            texture = "white_cube",
            collider = "box"
        )
class WallX2(Entity):
    def __init__(self,position=(14.5,0,-3)):
        super().__init__(
            parent = scene,
            model = "cube",
            scale = (30, 10, 5),
            position = position,
            color = color.gray,
            texture = "white_cube",
            collider = "box"
        )
class WallY1(Entity):
    def __init__(self,position=(0,0,5)):
        super().__init__(
            parent = scene,
            model = "cube",
            scale = (0.1, 10, 15),
            position = position,
            color = color.gray,
            texture = "white_cube",
            collider = "box"
        )
class WallY2(Entity):
    def __init__(self,position=(29.5,0,6)):
        super().__init__(
            parent = scene,
            model = "cube",
            scale = (0.1, 10, 15),
            position = position,
            color = color.gray,
            texture = "white_cube",
            collider = "box"
        )

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = "sphere",
            scale= 150,
            texture = "sky_default",
            position = (12,2,12),
            double_sided=True
        )


sky = Sky()

wally1 = WallY1()
wally2 = WallY2()
wallx1 = WallX1()
wallx2 = WallX2()
target = Target()

for z in range(15):
    for x in range(30):
        voxel = Voxel(position=(x,0,z),)

player = FirstPersonController(position=(12,2,0))
app.run()