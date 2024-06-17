import pygame
import sys
import math
#Initialize Pygame
pygame.init()

# Set up the display

WIDTH,HEIGHT = 800,600
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D transformation")

WHITE= (255, 255, 255)
BLACK =(0, 0, 0)

def translation(x1,y1,x2,y2,tx,ty):
    x1=x1+tx
    y1=y1+ty
    x2=x2+tx
    y2=y2+ty

    pygame.draw.line(screen,"WHITE",(x1,y1),(x2,y2))



def scaling(x3,y3,x4,y4,r,r1):
    pygame.draw.circle(screen,"orange",(x3,y3),r)
    r=r*r1
    pygame.draw.circle(screen,"red",(x4,y4),r)




def rotation(x1,y1,x2,y2,angle):
    pygame.draw.line(screen,"White",(x1,y1),(x2,y2))
    x2=x2*math.cos(angle)-y2*math.sin(angle)
    y2=x2*math.sin(angle)+y2*math.cos(angle)
    pygame.draw.line(screen,"red",(x1,y1),(x2,y2))




def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #clear the screen
        screen.fill(BLACK)
        #draw the line
        translation(0,0,100,100,5,5)
        scaling(200,100,300,300,50,2)
        rotation(300,300,100,300,0.8)
        pygame.display.flip()
if __name__=='__main__':
    main()