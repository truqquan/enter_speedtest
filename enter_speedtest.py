import pygame
import sys
import time

pygame.init() 
pygame.display.set_caption('ENTER SPEEDTEST')

res = (900,700)  
screen = pygame.display.set_mode(res)
width = screen.get_width()
height = screen.get_height()

color_white = (255,255,255)
color_black = (51,0,0)
color_light = (170,170,170) 
color_dark = (100,100,100)
color_blue = (0,0,255)
  
normalfont = pygame.font.SysFont('arial',30)
smallfont = pygame.font.SysFont('arial',15)
logo_font = pygame.font.SysFont('Rubik',100)

count = 0

def draw_text(text, font, text_col, x, y):
    img = normalfont.render(text, True, text_col)
    screen.blit(img, (x, y))

clock = pygame.time.Clock()
 
font = pygame.font.Font(None, 25)
 
frame_count = 0
frame_rate = 60
start_time = 10
total_seconds = start_time - (frame_count // frame_rate)
time = start_time
total_seconds2 = total_seconds

minutes = total_seconds // 60
seconds = total_seconds % 60
minutes2 = minutes
seconds2 = seconds

j = 0

while True:
	  
	for event in pygame.event.get():
	      
		if event.type == pygame.QUIT:
			pygame.quit()
		if time > 0:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					count = count + 1
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				count = 0
				frame_count = 0
				frame_rate = 60
				start_time = 10


	screen.fill((255, 195, 0))

	screen.blit(normalfont.render('COUNTED: ' , True , color_black) , (width/6.5+40,height/5))
	screen.blit(normalfont.render('CLICK SPACE TO RESET ' , True , color_black) , (width/6,height/2))
	draw_text(str(count), normalfont, color_white, width/3+30, height/5)



	total_seconds = start_time - (frame_count // frame_rate)
	if total_seconds < 0:
	    total_seconds = 0
	minutes = total_seconds // 60
	seconds = total_seconds % 60
	output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
	time = int(seconds)

	text = normalfont.render(output_string, True, color_black)
	screen.blit(text, [250, 280])

	if count > 1:
		frame_count += 1
	clock.tick(frame_rate)




	pygame.display.update() 