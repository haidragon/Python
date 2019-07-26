import pygame
from pygame.locals import *
import time
import random

#创建飞机的基类
class BasePlan(object):
    def __init__(self,screen_temp,x,y,image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)
        self.bullet_list = []#存储发射出去的子弹
        self.hit = False#表示是否要爆炸
        self.bomb_list = []
        #self.__creat_image()#调用这个方法向bomb_list中添加图片
        self.image_num = 0#用来记录while True的次数,当次数达到一定值时才显示一张爆炸的图,然后清空,,当这个次数再次达到时,再显示下一个爆炸效果的图片
        self.image_index = 0#用来记录当前要显示的爆炸效果的图片的序号
    def boom(self):
        self.hit = True
#创建飞机类
class HeroPlan(BasePlan):
    def __init__(self,screen_temp):
        BasePlan.__init__(self,screen_temp,210,700,"./feiji/hero1.png")
        self.__creat_image()
        #爆炸效果
    def __creat_image(self):
        self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n1.png"))
        self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n2.png"))
        self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n3.png"))
        self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n4.png"))

    def display(self):
        #如果被击中,就显示爆炸效果,否则显示普通的飞机效果
        if self.hit == True:
            self.screen.blit(self.bomb_list[self.image_index], (self.x, self.y))
            self.image_num += 1
            if self.image_num == 7:
                self.image_index += 1
                self.image_num = 0
            if self.image_index > 3:
                time.sleep(1)
                exit()
        else:
            self.screen.blit(self.image, (self.x, self.y))
            judge_list = []
            for bullet in self.bullet_list:
                bullet.display()
                bullet.move()
                #判断子弹是否越界
                if bullet.judge():
                    judge_list.append(bullet)
            for i in judge_list:
                self.bullet_list.remove(i)
    def move_left(self):
        self.x -= 10
    def move_right(self):
        self.x += 10
    def move_up(self):
        self.y -= 10
    def move_down(self):
        self.y += 10
    #创建开火方法
    def fire(self,enemy_temp):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y,enemy_temp))

class EnemyPlan(BasePlan):
    '''敌机的类'''
    def __init__(self,screen_temp):
        BasePlan.__init__(self,screen_temp,0,0,"./feiji/enemy0.png")
        #super.__init__()
        self.direction = "right"
        self.__creat_image()
        #爆炸效果
    def __creat_image(self):
        self.bomb_list.append(pygame.image.load("./feiji/enemy0_down1.png"))
        self.bomb_list.append(pygame.image.load("./feiji/enemy0_down2.png"))
        self.bomb_list.append(pygame.image.load("./feiji/enemy0_down3.png"))
        self.bomb_list.append(pygame.image.load("./feiji/enemy0_down4.png"))
    def display(self):
        if self.hit == True:
            print("self.image_index:%d"%self.image_index)
            print(self.bomb_list)
            self.screen.blit(self.bomb_list[self.image_index],(self.x,self.y))
            self.image_num += 1
            if self.image_num == 7:
                self.image_index += 1
                self.image_num = 0
            if self.image_index > 3:
                print("="*50)
                print(self.image_index)
                time.sleep(1)
                exit()
        else:
            self.screen.blit(self.image, (self.x, self.y))
            judge_list = []
            for bullet in self.bullet_list:
                bullet.display()
                bullet.move()
                # 判断子弹是否越界
                if bullet.judge():
                    judge_list.append(bullet)
            for i in judge_list:
                self.bullet_list.remove(i)
    def move(self):
        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5
        if self.x > 480 - 50:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"
    #创建开火方法
    def fire(self,hero_temp):
        #创建一个随机数，降低敌机创建子弹类的频率
        random_num = random.randint(1,100)
        if random_num == 20 or random == 99:
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y,hero_temp))

#创建键盘控制函数
def key_control(hreo_temp,enemy_temp):
    # 获取事件，如键盘输入
    for event in pygame.event.get():
        # 判断是否点击了退出按钮
        # 需要导入：from pygame.locals import *
        if event.type == QUIT:
            print("exit")
            exit()
        # 检测是否按键
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print("left")
                hreo_temp.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                print("right")
                hreo_temp.move_right()
            elif event.key == K_w or event.key == K_UP:
                print("up")
                hreo_temp.move_up()
            elif event.key == K_s or event.key == K_DOWN:
                print("down")
                hreo_temp.move_down()
            elif event.key == K_SPACE:
                print("space")
                hreo_temp.fire(enemy_temp)
            elif event.key == K_c:
                hreo_temp.boom()
            #设置时间间隔，降低资源占用率
            time.sleep(0.01)

#创建子弹的基类
class BaseBullet(object):
    def __init__(self,screen_temp,x,y,image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
#创建子弹类
class Bullet(BaseBullet):
    def __init__(self,screen_temp,x,y,enemy_temp):
        BaseBullet.__init__(self,screen_temp,x+40,y-20,"./feiji/bullet.png")
        self.enemy_temp = enemy_temp
    def move(self):
        self.y -= 5

        if self.y >= self.enemy_temp.y and self.y <= self.enemy_temp.y+39 and self.x >= self.enemy_temp.x and self.x <= self.enemy_temp.x + 51:
            print("self.x:%d" % self.x)
            print("self.enemy_temp.x:%d" % self.enemy_temp.x)
            print("self.y:%d" % self.y)
            print("self.enemy_temp.y:%d" % self.enemy_temp.y)
            self.enemy_temp.boom()
    def judge(self):
        if self.y < 0:
            return True
        else:
            return False
#创建敌机子弹类
class EnemyBullet(BaseBullet):
    def __init__(self,screen_temp,x,y,hero_temp):
        BaseBullet.__init__(self, screen_temp, x + 25, y + 40, "./feiji/bullet1.png")
        self.hero_temp = hero_temp
    def move(self):
        self.y += 1
        if self.y >= self.hero_temp.y and self.y <= self.hero_temp.y+124 and self.x >= self.hero_temp.x and self.x <= self.hero_temp.x + 100:
            print("self.x:%d" % self.x)
            print("self.hero_temp.x:%d" % self.hero_temp.x)
            print("self.y:%d"%self.y)
            print("self.hero_temp.y:%d"%self.hero_temp.y)
            self.hero_temp.boom()
    def judge(self):
        if self.y > 852:
            return True
        else:
            return False

#创建主方法
def main():
    #创建一个窗口
    screen = pygame.display.set_mode((480,852),0,32)
    #screen = pygame.display.set_mode((300, 600), 0, 32)
    #创建一个背景图片
    background = pygame.image.load("./feiji/background.png")
    #创建一个玩家飞机图片
    hero = HeroPlan(screen)
    #创建一个敌机
    enemy = EnemyPlan(screen)
    while True:
        #背景图片添加到窗口中
        screen.blit(background,(0,0))
        #玩家飞机添加到窗口中
        hero.display()
        #敌机添加到窗口中
        enemy.display()
        enemy.move()
        enemy.fire(hero)
        #刷新界面
        pygame.display.update()
        #获取键盘事件
        key_control(hero,enemy)
        #time.sleep(0.01)

if __name__ == "__main__":
    main()
