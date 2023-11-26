from model import *
import glm


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        # skybox
        self.skybox = AdvancedSkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        # floor
        n, s = 20, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z)))

        # bedrock
        n = 20
        for x in range(-n, n, 2):
            for z in range(-n, n, 2):
                add(Cube(app, pos=(x, -4, z), tex_id=4))


        #portal
        for i in range(1, 10, 2):
            add(Cube(app, pos=(15,0,i), tex_id=2))
        
        for i in range(2, 11,2):
            add(Cube(app, pos=(15,i,1), tex_id=2))

        for i in range(1, 10, 2):
            add(Cube(app, pos=(15,10,i), tex_id=2))
        
        for i in range(2,9,2):
            add(Cube(app, pos=(15,i,9), tex_id=2))
        #luz do portal
        for i in range(2,9,2):
            add(Cube(app, pos=(15, i, 7), tex_id=1))
        
        for i in range(2,9,2):
            add(Cube(app, pos=(15, i, 5), tex_id=1))
        
        for i in range(2,9,2):
            add(Cube(app, pos=(15, i, 3), tex_id=1))


        #motanha de feno
        for i in range(-9, -16, -2):
            add(Cube(app, pos=(-10, 0, i), tex_id=5))
        
        for i in range(-9, -16, -2):
            add(Cube(app, pos=(-12, 0, i), tex_id=5))
        
        for i in range(-9, -16, -2):
            add(Cube(app, pos=(-14, 0, i), tex_id=5))
        
        for i in range(-9, -16, -2):
            add(Cube(app, pos=(-8, 0, i), tex_id=5))
        
        for i in range(-9, -14, -2):
            add(Cube(app, pos=(i, 2, -10), tex_id=5))
        
        for i in range(-9, -14, -2):
            add(Cube(app, pos=(i, 2, -12), tex_id=5))
        
        for i in range(-9, -14, -2):
            add(Cube(app, pos=(i, 2, -14), tex_id=5))
       
        for i in range(-11, -14, -2):
            add(Cube(app, pos=(-10, 4, i), tex_id=5))
        
        for i in range(-11, -14, -2):
            add(Cube(app, pos=(-12, 4, i), tex_id=5))

        add(Cube(app, pos=(-11, 6, -12), tex_id=5))
        

        
        # moving cube
        self.moving_cube = MovingCube(app, pos=(0, 6, 8), scale=(3, 3, 3), tex_id=3)
        add(self.moving_cube)

    def update(self):
        self.moving_cube.rot.xyz = self.app.time
