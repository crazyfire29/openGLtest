import os

from opengl_shape.circle import Circle
from opengl_shape.image_circle_element import ImageCircleElement


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

    def create_item_race_illustration_circle(self, image_path, center, radius):
        unit_race_circle = ImageCircleElement(image_path=image_path,
                                              center=center,
                                              radius=radius)
        self.add_shape(unit_race_circle)

    def create_item_type_circle(self, color, center, radius):
        unit_attack_circle = Circle(color=color,
                                    center=center,
                                    radius=radius)
        self.add_shape(unit_attack_circle)


    def init_item_card(self, image_path,circle_radius):
        print(f"{image_path}")
        self.create_item_energy_circle(color=(1.0, 0.33, 0.34, 1.0),
                                       center=(0, 0),
                                       radius=circle_radius)

        self.create_item_race_illustration_circle(image_path=image_path,
                                                    center=(350, 0),
                                                    radius=circle_radius)

        self.create_item_type_circle(color=(0.988, 0.976, 0.800, 1.0),
                                     center=(350, 500),
                                     radius=circle_radius)