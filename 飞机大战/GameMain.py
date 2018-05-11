import pygame
from PlanSprite import *

#飞机大战主游戏
class PlaneGame(object):
	def __init__(self):
		#创建游戏的窗口
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		#游戏时钟
		self.clock = pygame.time.Clock()
		#调用私有方法，精灵和精灵组的创建
		self.__create_sprites()

		#定时器 毫秒
		#第一个参数是事件的名字
		#第二个参数是多长时间执行一次时间
		#设置定时器事件 - 每秒创建一架敌机
		self.screen = pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)

		#敌机的精灵组
		self.enemy_group = pygame.sprite.Group()

	def __create_sprites(self):
		bg1 = Background()
		bg2 = Background(True)
		self.back_group = pygame.sprite.Group(bg1,bg2)

		# 英雄组
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

	#事件监听
	def __event_handler(self):
		# pass
		for event in pygame.event.get():

		# 判断是否退出游戏
			if event.type == pygame.QUIT:
				PlaneGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:#定时器事件
				enemy = Enemy()
				self.enemy_group.add(enemy)
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
				self.hero.fire()

#1、随机x值 一定要有最大值 随机数
#2、初始化速度  随机1-?
#3、初始化y的位置
	def __check_collide(self):
		pass
		# 1. 子弹摧毁敌机
		pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

		# 2. 敌机撞毁英雄
		enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

		# 判断列表时候有内容
		if len(enemies) > 0:

			# 让英雄牺牲
			self.hero.kill()

			# 结束游戏
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
