import os

from opengl_shape.circle import Circle

class ItemCard:
    __imagePath = None

    def __init__(self, local_translation=(0, 0), scale=1):
        self.shapes = []
        self.local_translation = local_translation
        self.scale = scale

    def change_local_translation(self, _translation):
        self.local_translation = _translation

    def get_shapes(self):
        return self.shapes

    def add_shape(self, shape):
        shape.local_translate(self.local_translation)
        self.shapes.append(shape)

    def create_item_energy_circle(self, color, center, radius):
        unit_energy_circle = Circle(color=color,
                                    center=center,
                                    radius=radius)
        self.add_shape(unit_energy_circle)

    def create_item_race_circle(self, color, center, radius):
        unit_tribe_circle = Circle(color=color,
                                   center=center,
                                   radius=radius)
        self.add_shape(unit_tribe_circle)

    def create_item_type_circle(self, color, center, radius):
        unit_attack_circle = Circle(color=color,
                                    center=center,
                                    radius=radius)
        self.add_shape(unit_attack_circle)


    def init_shapes(self):

        circle_radius = 30
        self.create_item_energy_circle(color=(1.0, 0.33, 0.34, 1.0),
                                       center=(0, 0),
                                       radius=circle_radius)

        self.create_item_race_circle(color=(0.678, 0.847, 0.902, 1.0),
                                      center=(350, 0),
                                      radius=circle_radius)

        self.create_item_type_circle(color=(0.988, 0.976, 0.800, 1.0),
                                       center=(350, 500),
                                       radius=circle_radius)

    def redraw_shapes_with_scale(self, scale: float):
        print(f"scale : {scale}")

        self.shapes = []

        # self.scale = scale * self.scale
        self.scale = 3 / (scale + 1)
        rectangle_width = 350 * self.scale
        rectangle_height = 500 * self.scale

        print(f"local_translation = {self.local_translation}")
        self.local_translation = ((self.scale * self.local_translation[0]), 0)

        circle_radius = 30 * self.scale
        self.create_item_energy_circle(color=(1.0, 0.33, 0.34, 1.0),
                                       center=(0, 0),
                                       radius=circle_radius)

        self.create_item_race_circle(color=(0.678, 0.847, 0.902, 1.0),
                                      center=(rectangle_width, 0),
                                      radius=circle_radius)

        self.create_item_type_circle(color=(0.988, 0.976, 0.800, 1.0),
                                       center=(rectangle_width, rectangle_height),
                                       radius=circle_radius)
