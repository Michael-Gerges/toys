import pygame 
import sys
from pygame import *
pygame.init()
size_x = 800
size_y = 600
import random
win = pygame.display.set_mode((size_x, size_y))

back_ground_image =  pygame.image.load(r"C:\Users\micha\OneDrive\Desktop\1.jpg")
my_image_flipped = pygame.transform.flip(back_ground_image, False, True)
my_image_flipped = pygame.transform.scale(back_ground_image, (size_x, size_y))
# my_image_flipped = pygame.transform.rotate(back_ground_image, (size_x, size_y))


#pygame.mi­xer.init()
#pygame.mi­xer.mu­sic.load()
#pygame.mi­xer.mu­sic.play()
#pygame.mi­xer.mu­sic.stop()

colour = (0, 255, 255)
font = pygame.font.Font(None, 60)
location = (10, 10)



pygame.display.set_caption("my first game")
x,y,width,height,velocity = 1,1,40,60,1

enx,eny = size_x-width, size_y-height

a,b,c = 100,100,100
run = True
while run:

    #print(x)
    pygame.time.delay(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if x == 0 or x == win.get_rect().width-width or y==0 or y==win.get_rect().height-height:
        print("game over")
        pygame.quit()
        sys.exit()


    if keys[pygame.K_LEFT]:
        x -= velocity
    if keys[pygame.K_RIGHT]:
        x+=velocity
    if keys[pygame.K_UP]:
        y -= velocity
    if keys[pygame.K_DOWN]:
        y+=velocity

    if keys[pygame.K_a]:
        a+=1
        c-=1
    if keys[pygame.K_s]:
        b+=2
    if keys[pygame.K_d]:
        a-=1
        b-=1
    if keys[pygame.K_w]:
        c+=1  
    win.fill((0,0,0))
    win.blit(my_image_flipped, (0,0))
    if keys[pygame.K_k]:
        width += 1
    if keys[pygame.K_j]:
        width -= 1       
    if keys[pygame.K_m]:
        height += 1
    if keys[pygame.K_n]:
        height -= 1

    if a<0:
        a = 0
    if a > 255:
        a = 255
    if b<0:
        b = 0
    if b > 255:
        b = 255
    if c<0:
        c = 0
    if c > 255:
        c = 255
    enx += random.randint(-2,0)
    eny += random.randint(-2,0)
    pygame.draw.rect(win, (a,b,c), (x,y,width,height))
    pygame.draw.ellipse(win, 	(230,230,250), (enx,eny,width,height))
    uu ,mm = pygame.mouse.get_pos()

    if x < 20 or x> size_x-width-20 or y < 20 or y>size_y-height-20:
        win.blit(font.render("Carefull", True,	(128,0,128)), location)
        pygame.mouse.set_visible(False)
        win.blit(font.render("{} {}".format(uu, mm), True,(220,20,60)), (x,y))
    else:
        pygame.mouse.set_visible(True)

    pygame.display.update()
    pygame.display.set_mode((abs(x- enx), abs(y- eny)))
    #pygame.display.flip()
