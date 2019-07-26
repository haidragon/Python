import pygame
from pygame.locals import *
import time

def main():
    #创建一个窗口
    screen = pygame.display.set_mode((480,852),0,32)
    #创建一个背景图片
    background = pygame.image.load("./feiji/background.png")
    #创建一个玩家飞机图片
    hero = pygame.image.load("./feiji/hero1.png")
    x = 210
    y = 700
    while True:
        #背景图片添加到窗口中
        screen.blit(background,(0,0))
        #玩家飞机添加到窗口中
        screen.blit(hero,(x,y))
        #x += 1
        #刷新界面
        pygame.display.update()

        #获取事件，如键盘输入
        for event in pygame.event.get():
            #判断是否点击了退出按钮
            #需要导入：from pygame.locals import *
            if event.type == QUIT:
                print("exit")
                exit()
            #检测是否按键
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print("left")
                    x -= 5
                elif event.key == K_d or event.key == K_RIGHT:
                    print("right")
                    x += 5
                elif event.key == K_w or event.key == K_UP:
                    print("up")
                    y -= 5
                elif event.key == K_s or event.key == K_DOWN:
                    print("down")
                    y += 5
                elif event.key == K_SPACE:
                    print("space")


            #设置时间间隔，降低资源占用率
            time.sleep(0.1)

if __name__ == "__main__":
    main()
