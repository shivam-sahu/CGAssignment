#importing time
import time

#pygame imports
import pygame
from pygame.locals import *

#opengl imports
from OpenGL.GL import *
from OpenGL.GLU import *

# Variable Declaration
a = int(input(" What is value of a "))
b = int(input(" What is value of b "))
xs = 10


#defing functions for basic shapes
def drawPixel(x,y):
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def drawLine(a,b,c,d):
    glBegin(GL_LINES)
    glVertex2f(a,b)
    glVertex2f(c,d)
    glEnd()

#main drawing logic
def draw():
        #global declaration of a and b
        global a, b, xs
        
        #  print(a, b)

        # drawLine function is called
        drawLine(300, 750, 300, 750-a)
        drawLine(500, 750, 500, 750-b)
        
        #Delay is in seconds
        time.sleep(3)
        
#main function
def main():
    #boiler-plate setup code
    pygame.init()
    display = (1000,800) #the pygame windows resolution
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluOrtho2D(0,1000,800,0)

    global a, b

    #the main loop 
    while True:

        #event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Main Logic For EUCLID's 
        
        if (a != b):
                if (a < b):
                        b -= a
                else:
                        a -= b
                # time.sleep(1)
                draw()
        
        if ( a == b):
                print("GCD is ",a)
                break
                



        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #clear the frame
        draw() #calling the function with drawing logic
        pygame.display.flip() #bring up the updated screen

#calling main()
main()
