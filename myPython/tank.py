import pygame
import random

# Initialize Pygame
pygame.init()

# Game window size 
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tank Game")

# Define Tank class
class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.original_image = pygame.image.load("myPython/tank.png").convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1
        
    def move_left(self):
        self.rect.x -= self.speed
    
    def move_right(self):
        self.rect.x += self.speed
    
    def move_up(self):
        self.rect.y -= self.speed
    
    def move_down(self):
        self.rect.y += self.speed

# 创建敌人类
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 255, 0))  # 绿色
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.randint(1, 5)

    def update(self):
        self.rect.y += self.speed

# 创建所有精灵组
all_sprites = pygame.sprite.Group()

# 创建坦克对象
tank = Tank(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50)
all_sprites.add(tank)

# 创建敌人对象
enemy = Enemy(random.randint(0, WINDOW_WIDTH - 32), 0)
all_sprites.add(enemy)

# 游戏循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 处理键盘事件
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        tank.move_left()
    if keys[pygame.K_RIGHT]:
        tank.move_right()
    if keys[pygame.K_UP]:
        tank.move_up()
    if keys[pygame.K_DOWN]:
        tank.move_down()

    # 更新所有精灵
    all_sprites.update()

    # 检测碰撞
    if pygame.sprite.collide_rect(tank, enemy):
        # running = False
        enemy.rect.y = 0 # 重置敌人位置

    # 绘制背景和所有精灵
    window.fill((0, 0, 0))  # 黑色
    all_sprites.draw(window)

    # 更新屏幕
    pygame.display.update()

# 游戏结束
pygame.quit()

#这个示例创建了一个红色的坦克和一个绿色的敌人，
#当坦克和敌人碰撞时游戏结束。你可以根据自己的需要扩展这个示例，
# 比如添加更多的敌人、子弹、障碍物等等。