import pygame
import time
import random


pygame.init()

white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green= (0,200,0)

display_width=800
display_height=600
gameDisplay= pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Snaky Snake")

icon = pygame.image.load('apple.png')
pygame.display.set_icon(icon)

img = pygame.image.load('head.png')
appleimg =  pygame.image.load('apple.png')

clock=pygame.time.Clock();
fps=10
applethick= 30
block_size=20
direction = "right"
smallfont= pygame.font.SysFont("comicsansms",25)
medfont= pygame.font.SysFont("comicsansms",50)
largefont= pygame.font.SysFont("comicsansms",80)

def pause():
    paused =True
    message_scrn("Paused!",black,-100,"large")
        
    message_scrn("Press C to continue or Q to Quit",black,-200,"small")
    pygame.display.update()
        
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit
                    quit()
        
        clock.tick(5)
                    
                

def score(score):
    text=smallfont.render("Score "+str(score),True,black)
    gameDisplay.blit(text,[0,0])

def randapplegen():
    randapplex= round(random.randrange(0,display_width-applethick))#/10.0)*10.0 
    randappley= round(random.randrange(0,display_height-applethick))#/10.0)*10.0
    return randapplex,randappley

def game_intro():

    intro=True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro=False
                if event.key == pygame.K_q:
                    intro=False
                    pygame.quit()
                    quit()
                
                
        gameDisplay.fill(white)
        message_scrn("Snake And Apple",green,-100,"large")
        message_scrn("The Objective of the game is to eat apples",black,-30)
        message_scrn("Press c to Play!",black,50,"large")
        
        pygame.display.update()
        #clock.tick(3)
def snake(block_size, snakelist):

    if direction == "right":
        head= pygame.transform.rotate(img,270)
    elif direction == "left":
        head= pygame.transform.rotate(img,90)
    elif direction == "up":
        head= img
    elif direction == "down":
        head= pygame.transform.rotate(img,180)
    
    gameDisplay.blit(head,(snakelist[-1][0],snakelist[-1][1]))
    
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block_size,block_size])
        
def text_objects(text,color,size):
    if size=="small":
        textsurface =  smallfont.render(text,True,color)
    elif size=="medium":
        textsurface =  medfont.render(text,True,color)
    elif size=="large":
        textsurface =  largefont.render(text,True,color)
    
    return textsurface,textsurface.get_rect()

def message_scrn(msg,color,y_displace=0,size="small"):
    textsurf,textrect = text_objects(msg,color,size)
    textrect.center = (display_width / 2),(display_height/2)+y_displace
    gameDisplay.blit(textsurf,textrect)

    #screen_text = font.render(mag,True,color)
    #gameDisplay.blit(screen_text,[0,0])

def gameLoop():
    global direction
    gameExit = False
    gameOver= False
    lead_x=display_width/2
    lead_y=display_height/2
    lead_xc=0
    lead_yc=0

    snakelist = [] 
    snakel=1
        
    randapplex,randappley=randapplegen()
    while not gameExit:

        if gameOver== True:
           # gameDisplay.fill(white)
            message_scrn("Game Over",red,-50,"large")
            message_scrn("Press C to Play Again",black,50, "medium")
            message_scrn("Press Q to Exit",black,100,"medium")
            
            pygame.display.update()

        while gameOver== True:
            
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    gameExit= True
                    gameOver= False
                
                if event.type== pygame.KEYDOWN:
                    if event.key== pygame.K_q:
                        gameExit= True
                        gameOver= False
                    if event.key == pygame.K_c:
            
                        gameLoop()
                    
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                gameExit=True
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_LEFT:
                    lead_xc = -block_size
                    lead_yc = 0
                    direction="left"
                elif event.key== pygame.K_RIGHT:
                    lead_xc = block_size
                    lead_yc = 0
                    direction="right"
                elif event.key== pygame.K_UP:
                    lead_yc = -block_size
                    lead_xc = 0
                    direction="up"
                elif event.key== pygame.K_DOWN:
                    lead_yc = block_size
                    lead_xc = 0
                    direction="down"
                elif event.key== pygame.K_p:
                    pause()
    

                    
                    
        if lead_x >= display_width or lead_y>=display_height or lead_x<0 or lead_y<0:
            gameOver=True
            
        lead_x=lead_x+lead_xc
        lead_y=lead_y+lead_yc
        
        
        gameDisplay.fill(white)

        
        #pygame.draw.rect(gameDisplay,red,[randapplex,randappley,applethick,applethick])
        gameDisplay.blit(appleimg,(randapplex,randappley))
        
        snakehead= []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)

        if len(snakelist) > snakel:
            del snakelist[0]

        for es in snakelist[:-1]:
            if es==snakehead:
                gameOver= True
                 
        snake(block_size,snakelist)

        score(snakel- 1)
        
        pygame.display.update()

##        if lead_x >= randapplex and lead_x <= randapplex+applethick:
##            if lead_y >= randappley and lead_y <= randappley+applethick:
##                randapplex= round(random.randrange(0,display_width-block_size))#/10.0)*10.0 
##                randappley= round(random.randrange(0,display_height-block_size))#/10.0)*10.0
##                snakel+=snakel   

        if lead_x> randapplex and lead_x < randapplex+applethick or lead_x+block_size> randapplex and lead_x + block_size< randapplex + applethick:
            if lead_y > randappley and lead_y< randappley + applethick:
                randapplex,randappley=randapplegen()
                snakel=snakel+1   
            elif lead_y+ block_size > randappley and lead_y + block_size< randappley+ applethick:  
                randapplex,randappley=randapplegen()
                snakel=snakel+1
            
        clock.tick(fps)

    
    pygame.quit()
    quit()

game_intro()
gameLoop()
