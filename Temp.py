import pygame, sys,random

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()
width=800
height=400
screen = pygame.display.set_mode((width,height))

#load images
bg = pygame.image.load("bg.jpg").convert_alpha()
player = pygame.image.load("character2.png").convert_alpha()

arrow=pygame.Rect(130,251,50,2)

#create a state variable
state="ready"
while True:    
    screen.fill((50,150,255))
    screen.blit(bg,[0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Check if space key is pressed
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_SPACE:
                state="shoot"
    #create ready state
    if state == "ready":
        arrow.x=arrow.x=130
        
    #create shoot state
    if state=="shoot":
        arrow.x=arrow.x+15
         
    if arrow.x>800:
        state="ready"
   
    screen.blit(player,[100,200])  
    pygame.draw.rect(screen, [250,0,130], arrow)
    pygame.display.update()
    clock.tick(30)

