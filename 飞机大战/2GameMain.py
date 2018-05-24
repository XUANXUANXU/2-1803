import pygame
from PlanSprite import *

class PlaneGame(object):
	def __init__(self):
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		self.clock = pygame.time.Clock()
		self.__create_sprites()

		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)

		self.enemy_group = pygame.sprite.Group()

	def __create_sprites(self):
		bg1 = Background()
		bg2 = Background(True)
		self.back_group = pygame.sprite.Group(bg1,bg2)

		self.hero = Hero()
		self.hero_group = pygame.sprite.Group(self.hero)


	def start_game(self):
		print("游戏开始...")

		while  True:
			self.clock.tick(FRAME_PER_SEC)
			self.__event_handler()
			self.__check_collide()
			self.__update_sprites()
			pygame.display.update()	

	def __event_handler(self):
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				PlaneGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:#定时器事件
				enemy = Enemy()
				self.enemy_group.add(enemy)
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
				self.hero.fire()

	def __check_collide(self):
		pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

		enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

		if len(enemies) > 0:

			self.hero.kill()

			PlaneGame.__game_over()


	def __update_sprites(self):
		self.back_group.update()
		self.back_group.draw(self.screen)

		self.enemy_group.update()
		self.enemy_group.draw(self.screen)

		self.hero_group.update()
		self.hero_group.draw(self.screen)

		self.hero.bullets.update()
		self.hero.bullets.draw(self.screen)
	@staticmethod		
	def __game_over():
		pygame.quit
		exit()

if __name__ == '__main__':
	game = PlaneGame()
	game.start_game()
