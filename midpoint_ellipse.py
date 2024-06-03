import pygame
import sys

#Initialize Pygame
pygame.init()

# Set up the display
WIDTH,HEIGHT = 800,600
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint circle Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK =(0, 0, 0)


def midpoint_ellipse(xc, yc, rx, ry):
    x = 0
    y = ry
    p1 = (ry ** 2) - (rx ** 2) * ry + (1 / 4) * (rx ** 2)
    while (2 * (ry ** 2) * x) <= (2 * (rx ** 2) * y):
        screen.set_at((round(x + xc), round(y + yc)), WHITE)
        screen.set_at((round(x + xc), round(-y + yc)), WHITE)
        screen.set_at((round(-x + xc), round(y + yc)), WHITE)
        screen.set_at((round(-x + xc), round(-y + yc)), WHITE)
        x = x + 1
        if p1 < 0:
            y = y
            p1 = p1 + 2 * (ry ** 2) * x + (ry ** 2)
        else:
            y = y - 1
            p1 = p1 + 2 * (ry ** 2) * x - 2 * (rx ** 2) * y + (ry ** 2)

    p2 = (ry ** 2) * ((x + 1 / 2) ** 2) + (rx ** 2) * ((y - 1) ** 2) - (rx ** 2) * (ry ** 2)
    while y > 0:
        screen.set_at((round(x + xc), round(y + yc)), WHITE)
        screen.set_at((round(x + xc), round(-y + yc)), WHITE)
        screen.set_at((round(-x + xc), round(y + yc)), WHITE)
        screen.set_at((round(-x + xc), round(-y + yc)), WHITE)
        y = y - 1
        if p2 > 0:
            x = x
            p2 = p2 - 2 * (rx ** 2) * y + (rx ** 2)
        else:
            x = x + 1
            p2 = p2 + 2 * (ry ** 2) * x - 2 * (rx ** 2) * y + (rx ** 2)



def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #clear the screen
        screen.fill(BLACK)

        #draw the circle
        midpoint_ellipse(300,300,200,100)
        
        #update the display
        pygame.display.flip()
if __name__=='__main__':
    main()