import pygame, sys
from random import randint, uniform

from nave import *

# functions

def laser_update(laser_list, speed = 300):
	for rect in laser_list:
		rect.y -= speed * delta_time 
		if rect.bottom < 0:
			laser_list.remove(rect)

def meteor_update(meteor_list, speed = 200):
	for meteor_tuple in meteor_list:

		rect = meteor_tuple[0]
		direction = meteor_tuple[1]
		rect.center += speed * delta_time * direction

		if rect.top > height:
			meteor_list.remove(meteor_tuple)

def laser_return_to_shoot(laser_can_shoot, duration = 500):
	if not laser_can_shoot:
		current_time = pygame.time.get_ticks()
		if current_time - laser_time_to_shoot > duration:
			laser_can_shoot = True
	return laser_can_shoot

pygame.init()

width = 500
height = 500
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

# nave
nave = pygame.image.load('./assets/nave.png').convert_alpha()
nave_rect = nave.get_rect(center = (width/2,height/2))

# background
background = pygame.image.load('./assets/bg.png').convert()

# laser
laser = pygame.image.load('./assets/laser.png').convert_alpha()
laser_list = []
laser_can_shoot = True
laser_time_to_shoot = None

# meteor
meteor = pygame.image.load('./assets/meteor.png').convert_alpha()
meteor_list = []

# sprite Group
sprite_groupe_nave = pygame.sprite.GroupSingle()

nave_i = Nave(sprite_groupe_nave)

CALL_METEOR = pygame.event.custom_type()
pygame.time.set_timer(CALL_METEOR, 600)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN and laser_can_shoot:
			if event.button == 1:
				laser_rect = laser.get_rect(midbottom = nave_rect.midtop)
				laser_list.append(laser_rect)
				laser_can_shoot = False
				laser_time_to_shoot = pygame.time.get_ticks()

		if event.type == CALL_METEOR:

			x = randint(20, width - 20)
			y = randint(-150, -100)

			meteor_rect = meteor.get_rect(center = (x, y))

			vec_x = uniform(-0.5, 0.5)

			vec_direction = pygame.math.Vector2(vec_x, 1)

			meteor_list.append((meteor_rect, vec_direction))



	delta_time = clock.tick(120) / 1000
	keys = pygame.key.get_pressed()

	if keys[pygame.K_d]: 
		nave_rect.x += round(200 * delta_time)
	if keys[pygame.K_a]:
		nave_rect.x -= round(200 * delta_time)
	if keys[pygame.K_w]:
		nave_rect.y -= round(200 * delta_time)
	if keys[pygame.K_s]:
		nave_rect.y += round(200 * delta_time)


	# update section
	laser_update(laser_list, 400)
	meteor_update(meteor_list, 300)
	laser_can_shoot = laser_return_to_shoot(laser_can_shoot, 300)
	sprite_groupe_nave.update()

	screen.fill((255,127,127))
	screen.blit(background, (0,0))
	screen.blit(nave, nave_rect)
	sprite_groupe_nave.draw(screen)

	for rect in laser_list:
		screen.blit(laser, rect)

	for rect,_ in meteor_list:
		screen.blit(meteor, rect)

	for rect,_ in meteor_list:
		if rect.colliderect(nave_rect):
			print('GameOver')
			# -live

	for meteor_tuple in meteor_list:
		for laser_rect in laser_list:
			if laser_rect.colliderect(meteor_tuple[0]):
				laser_list.remove(laser_rect)
				meteor_list.remove(meteor_tuple)
	
	pygame.display.update()














































# fonts
# font = pygame.font.Font('./assets/ITC-Medea.ttf', 75) # True Type Font
# font_surface = font.render('Hello Font', True, (0,0,0))





