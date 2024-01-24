import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def drawText(x, y, text):
    font = pygame.font.SysFont('arial', 64)
    textSurface = font.render(text, True, (125, 125, 125, 255)).convert_alpha()
    textData = pygame.image.tostring(textSurface, "RGBA", True)
    glWindowPos2d(x-textSurface.get_width()/2, y-textSurface.get_height()/2)
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA,
                 GL_UNSIGNED_BYTE, textData)

pygame.init()
clock = pygame.time.Clock()
display = (640, 480)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    glRotatef(1, 3, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    drawText(display[0]/2, display[1]/2, "aaaadff")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()

if __name__ == '__main__':
    print("Hello World")