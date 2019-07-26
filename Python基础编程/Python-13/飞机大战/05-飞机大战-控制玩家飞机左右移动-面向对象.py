import pygame
from pygame.locals import *
import time

#创建飞机类
class HeroPlan():
    def __init__(self,screen_temp):
        self.x = 210
        self.y = 700
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/hero1.png")
        self.bullet_list = []#存储发射出去的子弹
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.y -= 1
            time.sleep(0.01)
    def move_left(self):
        self.x -= 5
    def move_right(self):
        self.x += 5
    def move_up(self):
        self.y -= 5
    def move_down(self):
        self.y += 5
    #创建开火方法
    def fire(self):
        self.bullet_list.append(Bullet(self.screen))


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
#创建主方法

#创建子弹类
class Bullet(object):
    def __init__(self,screen_temp):
        self.x = 210
        self.y = 700
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/bullet.png")
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

def main():
    #创建一个窗口
    screen = pygame.display.set_mode((480,852),0,32)
    #创建一个背景图片
    background = pygame.image.load("./feiji/background.png")
    #创建一个玩家飞机图片
    hero = HeroPlan(screen)

    while True:
        #背景图片添加到窗口中
        screen.blit(background,(0,0))
        #玩家飞机添加到窗口中
        hero.display()
        #刷新界面
        pygame.display.update()
        #获取键盘事件
        key_control(hero)




if __name__ == "__main__":
    main()
