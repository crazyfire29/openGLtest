import math

import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.raw.GLUT import glutSwapBuffers

from opengl_shape.circle import Circle
from opengl_shape.shape import Shape

from PIL import Image
from OpenGL import GL


class ImageCircleElement(Shape):
    def __init__(self, image_path, center, radius, global_translation=(0, 0), local_translation=(0, 0)):
        super().__init__([center], global_translation, local_translation)
        self.image_path = image_path
        self.radius = radius
        self.center = center
        self.is_visible = True

    def set_visible(self, visible):
        self.is_visible = visible

    def get_visible(self):
        return self.is_visible

    def draw(self):
        if self.get_visible():
            white_rect = Circle(color=(1.0, 1.0, 1.0, 1.0),
                                center=self.center,
                                radius=self.radius,
                                local_translation=self.local_translation,
                                global_translation=self.global_translation)
            white_rect.draw()

            image_data = self._load_image_data(self.image_path)
            # texture_ids = GL.glGenTextures(1)
            #
            # GL.glBindTexture(GL.GL_TEXTURE_2D, texture_ids)
            # GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_LINEAR)
            # GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_LINEAR)
            # GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_RGBA, image_data.shape[1], image_data.shape[0],
            #                 0, GL.GL_RGBA, GL.GL_UNSIGNED_BYTE, image_data)

            GL.glEnable(GL.GL_TEXTURE_2D)
            GL.glBindTexture(GL.GL_TEXTURE_2D, image_data)


            GL.glBegin(GL.GL_TRIANGLE_FAN)
            glColor3f(1.0, 1.0, 1.0)
            for i in range(360):
                theta = 2.0 * math.pi * i / 360
                x = self.radius * math.cos(theta) + self.vertices[0][0] + self.global_translation[0] + \
                    self.local_translation[0] - 1
                y = self.radius * math.sin(theta) + self.vertices[0][1] + self.global_translation[1] + \
                    self.local_translation[1] - 1
                glVertex2f(x, y)

            GL.glEnd()


            GL.glDisable(GL.GL_TEXTURE_2D)

    def _load_image_data(self, path):
        image = Image.open(path)
        image_data = image.tobytes("raw", "RGBX", 0, -1)

        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.width, image.height, 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        return texture_id


