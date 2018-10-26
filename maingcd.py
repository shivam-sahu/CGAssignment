#importing time
import time

#pygame imports
import pygame
from pygame.locals import *

#opengl imports
from OpenGL.GL import *
from OpenGL.GLU import *

# Variable Declaration
height = 800
width = 1000
a = int(input("What is value of a: "))
b = int(input("What is value of b: "))
mappingHeight = max(a, b)
xs = 10

lengths = [(a, b)]

# defing functions for basic shapes
def drawPixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def drawLine(a, b, c, d):
    glBegin(GL_LINES)
    glVertex2f(a, b)
    glVertex2f(c, d)
    glEnd()

def drawRect(a, b, c, d):
    drawLine(a-10, b, c-10, d) # left line
    drawLine(a+10, b, c+10, d) # right line
    drawLine(a-10, d, c+10, d) # upper line
    drawLine(a-20, b, c+20, b) # lower line

def drawFilledRect(a, b, c, d):
    drawLine(a-20, b, c+20, b) # lower line
    d = int(d)
    # print(type(b), type(d), b, d)
    for x in range(d, b):
        drawLine(a-10, x, c+10, x)

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


# main drawing logic
def draw():
        #global declaration of a and b
        global a, b, xs
        global height, lengths

        # When a is equal to b , we have required H.C.F

        dist = width / len(lengths)

        for x in range(len(lengths)):
            tempDist = dist / 2 + dist * x

            tempA = translate(lengths[x][0], 0, mappingHeight, 0, height - 40)
            tempB = translate(lengths[x][1], 0, mappingHeight, 0, height - 40)

            drawFilledRect(tempDist - 20, height - 20, tempDist - 20, height - tempA - 20)
            drawFilledRect(tempDist + 20, height - 20, tempDist + 20, height - tempB - 20)

        #Delay is in seconds
        time.sleep(1)


#main function
def main():
    #boiler-plate setup code
    pygame.init()
    display = (width, height)  # the pygame windows resolution
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(0, 1000, 800, 0)
    glClear(GL_COLOR_BUFFER_BIT |GL_DEPTH_BUFFER_BIT)  # clear the frame
    glClearColor(0.607, 0.278, 0.3, 1)  # set background color

    global a, b
    global lengths

    #the main loop
    while True:

        #event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT |GL_DEPTH_BUFFER_BIT)  # clear the frame
        glClearColor(0.607, 0.278, 0.3, 1)  # set background color
        draw()  # calling the function with drawing logic
        pygame.display.flip()  # bring up the updated screen

        if(a != b):
            if(a > b):
                a -= b
            else:
                b -= a
            lengths += [(a, b)]
            print(lengths)
        else:
            print(f"The GCD is {lengths[len(lengths) - 1][0]}")
            input("Press any key to exit!")
            pygame.quit()
            quit()


#calling main()
main()
