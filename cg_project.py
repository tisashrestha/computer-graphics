import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Underwater Scene")

BLUE = (0, 128, 255)
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (169, 169, 169)
GREEN = (50, 205, 50)



def draw_fish(x, y, size, color):
    body_width = size * 2
    body_height = size
    tail_length = size

    #Body
    pygame.draw.ellipse(screen, color, (x, y, body_width, body_height))

    #Tail
    tail_points = [
        (x + body_width, y + body_height / 2),
        (x + body_width + tail_length, y),
        (x + body_width + tail_length, y + body_height)
    ]
    pygame.draw.polygon(screen, color, tail_points)

    #Fins
    fin_length = size / 2

    #upper fin
    pygame.draw.polygon(screen, color, [(x + body_width / 3, y + 10),
                                        (x + body_width / 1.5, y - body_height*0.75),
                                        (x + body_width/1.5, y  - fin_length *0.5)])
    
    #lower fin
    pygame.draw.polygon(screen, color, [(x + body_width / 3, y + body_height*0.9 ),
                                        (x + body_width / 1.5, y + body_height*1.25),
                                        (x + body_width/1.5, y  + body_height*0.9 + fin_length*1.5)])


    #eye
    eye_radius = size // 10
    pygame.draw.circle(screen, WHITE, (int(x + size * 0.3), int(y + size / 2)), eye_radius)



def draw_shark(x, y, size):
    body_width = size * 3
    body_height = size
    fin_length = size * 0.75

    #Body
    pygame.draw.ellipse(screen, GRAY, (x, y, body_width, body_height))
    fin_points = [
        (x + body_width / 3, y),  #Top middle of the body
        (x + body_width / 2.5 + fin_length, y - fin_length),  #upper right
        (x + body_width / 2.5 + fin_length, y ) ]   #lower right
    pygame.draw.polygon(screen, GRAY, fin_points)
 

    #Tail
    tail_points = [
        (x + body_width, y + body_height / 2),
        (x + body_width + fin_length, y),
        (x + body_width + fin_length, y + body_height)
    ]
    pygame.draw.polygon(screen, GRAY, tail_points)

    #Eye
    eye_radius = size // 8
    pygame.draw.circle(screen, WHITE, (int(x + size * 0.5), int(y + size *0.5)), eye_radius)



def draw_submarine(x, y, size):
    body_width = size * 4
    body_height = size * 1.5

    #Body
    pygame.draw.ellipse(screen, RED, (x, y, body_width, body_height))

    #Tower
    pygame.draw.rect(screen, RED, (x + size * 1.5, y - size, size, size))

    #Windows
    for i in range(3):
        pygame.draw.circle(screen, WHITE, (int(x + size * (i * 1.2 + 1)), int(y + size * 0.75)), size // 4)



def draw_bubbles(bubbles):
    for bubble in bubbles:
        pygame.draw.circle(screen, WHITE, (bubble[0], bubble[1]), bubble[2])

# Main loop
def main():
    clock = pygame.time.Clock()
    running = True

    # Initial positions and properties of the fish
    fish1_x, fish1_y = 300, 300
    fish2_x, fish2_y = 400, 400
    fish3_x, fish3_y = 500, 200
    fish_size = 50
    fish_speed1 = -5  #direction of fish->movement direction
    fish_speed2 = -7  
    fish_speed3 = -6  

    
    shark_x, shark_y = 100, 100
    shark_size = 60
    shark_speed = -4

    
    submarine_x, submarine_y = 50, 450
    submarine_size = 30
    submarine_speed = 2

    # Initial bubbles
    bubbles = []
    for _ in range(20):
        x = random.randint(0, WIDTH)
        y = random.randint(HEIGHT // 2 , HEIGHT)
        radius = random.randint(2, 5)
        bubbles.append((x, y, radius))      #add bubbles to the list

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move fish horizontally
        fish1_x += fish_speed1
        fish2_x += fish_speed2
        fish3_x += fish_speed3

      
        shark_x += shark_speed

     
        submarine_x += submarine_speed

        #fish cominng again after it goes off screen
        if fish1_x < -fish_size * 2:
            fish1_x = WIDTH
        if fish2_x < -fish_size * 2:
            fish2_x = WIDTH
        if fish3_x < -fish_size * 2:
            fish3_x = WIDTH

        
        if shark_x < -shark_size * 3:
            shark_x = WIDTH

    
        if submarine_x > WIDTH:
            submarine_x = -submarine_size * 4

        screen.fill(BLUE) 


        #fish
        draw_fish(fish1_x, fish1_y, fish_size, ORANGE)
        draw_fish(fish2_x, fish2_y, fish_size, YELLOW)
        draw_fish(fish3_x, fish3_y, fish_size, GREEN)

        #shark
        draw_shark(shark_x, shark_y, shark_size)

        #submarine
        draw_submarine(submarine_x, submarine_y, submarine_size)

        #draw bubbles
        draw_bubbles(bubbles)
        for i in range(len(bubbles)):       #iterates over each bubble in bubble list
            bubbles[i] = (bubbles[i][0], bubbles[i][1] - 1, bubbles[i][2])
            if bubbles[i][1] < 0:
                bubbles[i] = (random.randint(0, WIDTH), HEIGHT, bubbles[i][2])

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()