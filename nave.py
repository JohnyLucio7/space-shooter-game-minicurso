import pygame

class Nave(pygame.sprite.Sprite):
	def __init__(self, group):
		super().__init__(group)
		self.image = pygame.image.load('./assets/nave.png').convert_alpha()
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y += 1







