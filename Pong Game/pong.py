import pygame, sys, random
pygame.init()
clock = pygame.time.Clock()

screen_width = 1100
screen_height = 600
display_width=1100
display_height=600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')
gameDisplay=screen

light_grey = (200,200,200)
bg_color =dark_grey= pygame.Color('grey12')
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green= (0,200,0)

p1score=0
p2score=0
smallfont= pygame.font.SysFont("comicsansms",25)
medfont= pygame.font.SysFont("comicsansms",50)
largefont= pygame.font.SysFont("comicsansms",80)

#fire_sound = pygame.mixer.Sound("boom.wav")
#explosion_sound = pygame.mixer.Sound("a.wav")
pygame.mixer.music.load("a.mpeg")

def ball_animation():

	global ball_speed_x, ball_speed_y
	global p1score,p2score
	ball.x += ball_speed_x

	ball.y += ball_speed_y

	if ball.top <= 0 or ball.bottom >= screen_height:

		ball_speed_y *= -1

	if ball.left <= 0 or ball.right >= screen_width:

		ball_start()
	if ball.colliderect(player): 

		ball_speed_x *= -1
		p2score=p2score+1
		#pygame.mixer.Sound.play(explosion_sound)
		pygame.mixer.music.play(1)
		#ball_speed_x=ball_speed_x - 1
		#ball_speed_y=ball_speed_y - 1

	if ball.colliderect(opponent): 

		ball_speed_x *= -1
		p1score=p1score+1
		#pygame.mixer.Sound.play(explosion_sound)
		pygame.mixer.music.play(1)
		#ball_speed_x=ball_speed_x + 1
		#ball_speed_y= ball_speed_y + 1

	




def player_animation():

	player.y += player_speed
	if player.top <= 0:

		player.top = 0

	if player.bottom >= screen_height:

		player.bottom = screen_height

def opponent_animation():

	opponent.y += opponent_speed
	if opponent.top <= 0:

		opponent.top = 0

	if opponent.bottom >= screen_height:

		opponent.bottom = screen_height

def opponent_ai():

	if opponent.top < ball.y:

		opponent.y += opponent_speed

	if opponent.bottom > ball.y:

		opponent.y -= opponent_speed

	if opponent.top <= 0:

		opponent.top = 0

	if opponent.bottom >= screen_height:

		opponent.bottom = screen_height

def ball_start():

	global ball_speed_x, ball_speed_y

	ball.center = (screen_width/2, screen_height/2)

	ball_speed_y *= random.choice((1,-1))

	ball_speed_x *= random.choice((1,-1))

def score1(score):
    text=smallfont.render("Player1 Score "+str(score),True,light_grey)
    gameDisplay.blit(text,[180,0])
def score2(score):
    text=smallfont.render("Player2 Score "+str(score),True,light_grey)
    gameDisplay.blit(text,[700,0])
    
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

def game_intro(gameDisplay,color):

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
                
                
        gameDisplay.fill(color)
        message_scrn("Ping Pong",light_grey,-100,"large")
        #message_scrn("The Objective of the game is to eat apples",black,-30)
        message_scrn("Press c to Play!",light_grey,50,"medium")
        message_scrn("Player 1: W,S",light_grey,150,"medium")
        message_scrn("Player 2: Up,Down",light_grey,200,"medium")
        
        
        pygame.display.update()

# General setup



game_intro(screen,dark_grey)

ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10,140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10,140)


ball_speed_x = 10 * random.choice((1,-1))
ball_speed_y = 10 * random.choice((1,-1))
player_speed = 0
opponent_speed = 0



while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_UP:

				player_speed -= 10

			if event.key == pygame.K_DOWN:

				player_speed += 10
			if event.key == pygame.K_w:

				opponent_speed -= 10
			if event.key == pygame.K_s:

				opponent_speed += 10
	


		if event.type == pygame.KEYUP:

			if event.key == pygame.K_UP:

				player_speed = 0

			if event.key == pygame.K_DOWN:

				player_speed = 0
			if event.key == pygame.K_w:

				opponent_speed = 0
			if event.key == pygame.K_s:

				opponent_speed = 0

				
                
	ball_animation()

	player_animation()
	opponent_animation()
	
	screen.fill(bg_color)
	score1(p1score)
	score2(p2score)
	pygame.draw.rect(screen, light_grey, player)

	pygame.draw.rect(screen, light_grey, opponent)

	pygame.draw.ellipse(screen, light_grey, ball)

	pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0),(screen_width / 2, screen_height))
	
        
	pygame.display.flip()

	clock.tick(60)
