import pygame, sys

pygame.init()

# colocar elementos na tela
# mover esses elementos

largura = 500
altura = 500

cor_branca = (255, 255, 255)
tamanho_da_surface = (32,32)

tela = pygame.display.set_mode((largura, altura))

retangulo = pygame.Surface(tamanho_da_surface)
retangulo2 = pygame.Surface(tamanho_da_surface)

nave = pygame.image.load('./assets/nave.png').convert_alpha()
nave_rect = nave.get_rect()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# cores em rgb
	# R 0 - 255
	# G 0 - 255
	# B 0 - 255

	# retangulos 
  # imagens
  # fonts

	tela.fill((127,127,127))
	retangulo.fill('red')
	retangulo2.fill('blue')

	tela.blit(retangulo2, (55, 50))
	tela.blit(retangulo, (50, 50))
	tela.blit(nave, nave_rect)

	nave_rect.x += 1
	
	pygame.display.update()




