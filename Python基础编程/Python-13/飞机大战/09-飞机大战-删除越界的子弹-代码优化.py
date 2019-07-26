import pygame
from pygame.locals import *
import time

#创建飞机类
class HeroPlan():
    def __init__(self,screen_temp):
        self.x = 210
        self.y = 700
        #self.x = 100
        #self.y = 500
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/hero1.png")
        self.bullet_list = []#存储发射出去的子弹
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        judge_list = []
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            #判断子弹是否越界
            if bullet.judge():
                #self.bullet_list.remove(bullet)
                judge_list.append(bullet)
        for i in judge_list:
            self.bullet_list.remove(i)
            #time.sleep(0.01)
    def move_left(self):
        self.x -= 10
    def move_right(self):
        self.x += 10
    def move_up(self):
        self.y -= 10
    def move_down(self):
        self.y += 10
    #创建开火方法
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))

class EnemyPlan():
    '''敌机的类'''
    def __init__(self,screen_temp):
        self.x = 0
        self.y = 0
        self.direction = "right"
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/enemy0.png")
        self.bullet_list = []#存储发射出去的子弹
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            #time.sleep(0.01)
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
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))

#创建键盘控制函数
def key_control(hreo_temp):
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
                hreo_temp.fire()
            #设置时间间隔，降低资源占用率
            time.sleep(0.01)

#创建子弹类
class Bullet(object):
    def __init__(self,screen_temp,x,y):
        self.x = x+40
        self.y = y-20

        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/bullet.png")
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move(self):
        self.y -= 1
    def judge(self):
        if self.y < 200:
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
        #刷新界面
        pygame.display.update()
        #获取键盘事件
        key_control(hero)
        #time.sleep(0.01)

if __name__ == "__main__":
    main()
