import random
import pygame
#游戏屏幕大小
SCREEN_RECT = pygame.Rect(0,0,480,700)

#刷新帧率
FRAME_PER_SEC = 60

#敌机事件的常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
#爆炸图片
bg1 = pygame.image.load('./images/1.png')
bg2 = pygame.image.load('./images/2.png')
bg3 = pygame.image.load('./images/3.png')
bg4= pygame.image.load('./images/4.png')

#爆炸的精灵组
enemy1_down_group = pygame.sprite.Group()

#把爆炸图片放到列表中
enemy1_down_surface = []
enemy1_down_surface.append(bg1)
enemy1_down_surface.append(bg2)
enemy1_down_surface.append(bg3)
enemy1_down_surface.append(bg4)


#游戏精灵基类
class GameSprite(pygame.sprite.Sprite):
	def __init__(self,image_name,speed=1):
		super().__init__()
		#加载图像
		self.image = pygame.image.load(image_name)
		#设置尺寸大小
		self.rect = self.image.get_rect()
		#记录速度
		self.speed = speed
	#默认在垂直方向移动
	def update(self):
		self.rect.y += self.speed
	
#背景精灵
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
#敌机精灵
class Enemy(GameSprite):

	def __init__(self):
		image_name = "./images/en.png"
		super().__init__(image_name)
		self.speed = random.randint(1,3)
		
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)

		self.rect.bottom = 0
		self.down_index = 0 #敌机销毁图片索引
	def __del__(self):
		print("敌机挂了 %s" % self.rect)

	#调用父类方法，让敌机在垂直方向运动
	def update(self):
		super().update()

		if self.rect.y >= SCREEN_RECT.height:
			self.kill()
			print("敌机飞出屏幕...")

#英雄精灵
class Hero(GameSprite):
	def __init__(self):
		image_name = "./images/zhanji.png"
		super().__init__(image_name,0)
		
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 10
		# 创建子弹的精灵组
		self.bullets = pygame.sprite.Group()

	def update(self):
		# 获取用户按键
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
		#控制英雄的边界
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > SCREEN_RECT.bottom:
			self.rect.bottom = SCREEN_RECT.bottom
	#开火
	def fire(self):
		bullet = Bullet()

		# 2. 设置子弹精灵的位置
		bullet.rect.bottom = self.rect.y - 20
		bullet.rect.centerx = self.rect.centerx

		# 3. 将精灵添加到精灵组
		self.bullets.add(bullet)

		print("发射子弹...")
class Bullet(GameSprite):
	def __init__(self):
		super().__init__("./images/QQ图片.png", -10)
	def update(self):
		super().update()
	# 判断是否超出屏幕，如果是，从精灵组删除
		if self.rect.bottom < 0:
			self.kill()

