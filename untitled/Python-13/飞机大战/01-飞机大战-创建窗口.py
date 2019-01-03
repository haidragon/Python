import pygame
import time
def main():
    while "1":
        screen = pygame.display.set_mode((480,852),0,32)
        background = pygame.image.load("./feiji/background.png")
        while True:
            screen.blit(background,(0,0))
            pygame.display.update()
            time.sleep(0.1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()


if __name__ == "__main__":
    main()
