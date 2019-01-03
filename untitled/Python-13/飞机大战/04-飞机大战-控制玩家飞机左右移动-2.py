import pygame
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
        x += 1
        #刷新界面
        pygame.display.update()
        time.sleep(0.1)
        #

if __name__ == "__main__":
    main()
