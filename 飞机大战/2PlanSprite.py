import random
import pygame
SCREEN_RECT = pygame.Rect(0,0,480,700)

FRAME_PER_SEC = 60

CREATE_ENEMY_EVENT = pygame.USEREVENT

class GameSprite(pygame.sprite.Sprite):
	def __init__(self,image_name,speed=1):
		super().__init__()
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()
		self.speed = speed
	def update(self):
		self.rect.y += self.speed
	
class Background(GameSprite):

	def __init__(self,is_alt=False):
		image_name = "./images/xuan.png"
		super().__init__(image_name)
		if is_alt:
			self.rect.y = -self.rect.height

	def update(self):
		super().update()
		if self.rect.y > SCREEN_RECT.height:
			self.rect.y = -self.rect.height
class Enemy(GameSprite):

	def __init__(self):
		image_name = "./images/enen.png"
		super().__init__(image_name)
		self.speed = random.randint(1,3)
		
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)

		self.rect.bottom = 0
	def __del__(self):
		print("敌机挂了 %s" % self.rect)

	def update(self):
		super().update()

		if self.rect.y >= SCREEN_RECT.height:
			self.kill()
			print("敌机飞出屏幕...")

class Hero(GameSprite):
	def __init__(self):
		image_name = "./images/zhanji.png"
		super().__init__(image_name,0)
		
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120
		self.bullets = pygame.sprite.Group()

	def update(self):
		self.speed = 10
		keys_pressed = pygame.key.get_pressed()

		if keys_pressed[pygame.K_RIGHT]:
			self.rect.x += self.speed
		if keys_pressed[pygame.K_LEFT]:
			self.rect.x -= self.speed
		if keys_pressed[pygame.K_UP]:
			self.rect.y -= self.speed
		if keys_pressed[pygame.K_DOWN]:
			self.rect.y += self.speed
		if keys_pressed[pygame.K_SPACE]:
			self.fire()

		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > SCREEN_RECT.bottom:
			self.rect.bottom = SCREEN_RECT.bottom

	def fire(self):
		bullet = Bullet()

		bullet.rect.bottom = self.rect.y - 20
		bullet.rect.centerx = self.rect.centerx

		self.bullets.add(bullet)

		print("发射子弹...")
class Bullet(GameSprite):
	def __init__(self):
		super().__init__("./images/QQ图片.png", -10)
	def update(self):
		super().update()
		if self.rect.bottom < 0:
			self.kill()

