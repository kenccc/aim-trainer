from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from random import uniform

#defining variables
app = Ursina()
totalClicks = 0
score = 0
yScale = (0.1, 10, 15)

#creating classes and functions
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
            shader=lit_with_shadows_shader,
         )
def display_results():
    num = score/totalClicks
    window = WindowPanel(title=f"Score: {score}\n Missed: {totalClicks - score}, Accuracy: {int(num*100)}%",
                         content= f"Accuracy: {totalClicks/score}%")
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
            shader=lit_with_shadows_shader,
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
class Wall(Entity):
    def __init__(self,position=(14.5,0,15), scale = (30, 10, 5)):
        super().__init__(
            parent = scene,
            model = "cube",
            scale = scale,
            position = position,
            color = color.gray,
            texture = "white_cube",
            collider = "box",
            shader=lit_with_shadows_shader
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

#calling the classes
wallx1 = Wall()
sky = Sky()
wallx2 = Wall(position=(14.5,0,-3))
wally1 = Wall(position=(0,0,5),scale=yScale)
wally2 = Wall(position=(29.5,0,6),scale=yScale)
player = FirstPersonController(position=(12,2,0))
target = Target()

#creating the floor
for z in range(15):
    for x in range(30):
        voxel = Voxel(position=(x,0,z),)

#running the app
app.run()