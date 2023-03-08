import pygame as pg
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

pg.init()

(width,height) = (800,450)
canvas = pg.display.set_mode((width, height))
clock = pg.time.Clock()

CYAN = (0, 255, 255)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0, 255, 0)
BLUE=(0,0,255)
BLACK=(0,0,0)
BOTTOM=(51, 252, 40)
TREE_BOTTOM=(153,89,49)
LEAFS=(57,138,30)
BASE=(189,203,240)
cloud_one_x = 650   
cloud_one_y = 150
cloud_two_x = 500
cloud_two_y = 112
cloud_three_x = 600
cloud_three_y = 60

# cloud function, parameters are size of cloud
def cloud(xc, yc):
  # always the first drawing command
    pg.draw.circle(canvas, (211, 211, 211), (xc, yc), 50)
    pg.draw.circle(canvas, (211, 211, 211), (xc - 50, yc), 30)
    pg.draw.circle(canvas, (211, 211, 211), (xc + 50, yc), 30)



running = True
while running:
    # EVENT HANDLING
    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    
    canvas.fill(CYAN) # paint background

    #draw sun
    pg.draw.circle(canvas, (255, 255, 0), (700, 80), 60)

    cloud_one_x += 1
    cloud_two_x += 1
    cloud_three_x += 1
    if cloud_two_x-250>640:
        cloud_one_x=150
        cloud_two_x = 0
        cloud_three_x = 100
        
    cloud(cloud_one_x, cloud_one_y)
    cloud(cloud_two_x, cloud_two_y)
    cloud(cloud_three_x, cloud_three_y)
    
    # Draw Bottom
    pg.draw.rect(canvas, BOTTOM, [0, 350, 800, 250], 0)
    # Draw Trees
    pg.draw.rect(canvas, TREE_BOTTOM, [50, 280, 30, 100], 0)
    pg.draw.rect(canvas, TREE_BOTTOM, [420, 280, 30, 100], 0)
    # Draw Leaf
    pg.draw.circle(canvas, LEAFS, (435,280), 30)
    pg.draw.circle(canvas, LEAFS, (65,280), 30)
    #Draw Home base
    pg.draw.rect(canvas, BASE, [105,120,290,260], 0)
    #Draw home top
    pg.draw.polygon(canvas, RED, [[75,120], [430,120], [245, 5]], 0)
    #Draw windows
    pg.draw.rect(canvas, BLACK, [155, 155, 30, 30], 0)
    pg.draw.rect(canvas, BLACK, [235, 155, 30, 30], 0)
    pg.draw.rect(canvas, BLACK, [315, 155, 30, 30], 0)

    pg.draw.rect(canvas, BLACK, [155, 215, 30, 30], 0)
    pg.draw.rect(canvas, BLACK, [235, 215, 30, 30], 0)
    pg.draw.rect(canvas, BLACK, [315, 215, 30, 30], 0)
  
    pg.draw.rect(canvas, BLACK, [155, 275, 30, 30], 0)
    pg.draw.rect(canvas, BLACK, [235, 275, 30, 30], 0)
    pg.draw.rect(canvas, BLACK, [315, 275, 30, 30], 0)
  
    #Draw door
    pg.draw.rect(canvas, WHITE, [190, 315, 30, 65], 0)
    pg.draw.rect(canvas, WHITE, [290, 315, 30, 65], 0)
    
    pg.draw.rect(canvas, BLACK, [200, 340, 20, 10], 0)
    pg.draw.rect(canvas, BLACK, [290, 340, 20, 10], 0)

    # Draw the Car
    # Base of car
    pg.draw.rect(canvas, BLUE, [550,300,150,50])
    # Wheels
    pg.draw.circle(canvas, BLACK, (580,350), 15)
    pg.draw.circle(canvas, BLACK, (670,350), 15)
    # Top of Car
    pg.draw.line(canvas, BLACK, (625, 300), (625, 250))
    pg.draw.line(canvas, BLACK, (575, 300), (675, 300))
    pg.draw.line(canvas, BLACK, (610, 250), (575, 300))
    pg.draw.line(canvas, BLACK, (610, 250), (640, 250))
    pg.draw.line(canvas, BLACK, (640, 250), (675, 300))

    
    pg.display.flip()
    clock.tick(40)


pg.quit()