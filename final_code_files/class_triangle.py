
import random
class Triangle:
    def __init__(self, horizontal_width, vertical_height):
        self.triangle_color = (random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255))
        self.transparent_factor = random.randint(0,255)
        self.vertices = [
        (random.randint(0, horizontal_width), random.randint(0, vertical_height)),
        (random.randint(0, horizontal_width), random.randint(0, vertical_height)),
        (random.randint(0, horizontal_width), random.randint(0, vertical_height))]