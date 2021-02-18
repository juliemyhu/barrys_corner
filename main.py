""" pygame """
import pygame
from random import randint, randrange
from pygame.time import Clock
import time
import pygame.math as math
""" main loop for Barrys Corner"""

# toy

click = False


# define a main function
def main():

    # initialize the pygame module
    pygame.init()

    # load and set the logo
    logo = pygame.image.load("pawprint.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Barry's Corner")

    bg = pygame.image.load('wood.png')

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((2500, 1300))

    #Toy
    orange_ball = pygame.image.load('orange_ball.png')
    orange_ball = pygame.transform.scale(orange_ball, (300, 300))
    toyX = 1000
    toyY = 650
    toyX_change = 0
    toyY_change = 0

    pygame.display.flip()

    def toy(x, y):
        screen.blit(orange_ball, (x, y))

    running = True

    # main loop
    while running:

        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    toyX_change = -50
                if event.key == pygame.K_RIGHT:
                    toyX_change = 50
                if event.key == pygame.K_UP:
                    toyY_change = -50
                if event.key == pygame.K_DOWN:
                    toyY_change = 50
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    toyX_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    toyY_change = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        toyX += toyX_change
        toyY += toyY_change

        if toyX <= -40:
            toyX = -40
        elif toyX >= 2225:
            toyX = 2225
        if toyY <= -20:
            toyY = -20
        elif toyY >= 1070:
            toyY = 1070

        toy(toyX, toyY)
        pygame.display.update()


def main_menu():

    # initialize the pygame module
    pygame.init()

    # load and set the logo
    logo = pygame.image.load("pawprint.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Barry's Corner")

    bg = pygame.image.load('wood.png')
    barry_logo = pygame.image.load('barry_logo.png')

    screen = pygame.display.set_mode((2500, 1300))
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    start_game = myfont.render('Start Game', False, (0, 0, 0))
    random_mode = myfont.render('Random Mode', False, (0, 0, 0))

    while True:
        screen.blit(bg, (0, 0))

        bg = pygame.image.load('wood.png')
        bear = pygame.image.load('bear.png')

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(1500, 400, 280, 90)
        button_2 = pygame.Rect(1500, 600, 280, 90)

        if button_1.collidepoint((mx, my)):
            if click:
                main()
        if button_2.collidepoint((mx, my)):
            if click:
                random_game()
        pygame.draw.rect(screen, (
            255,
            255,
            255,
        ), button_1)
        pygame.draw.rect(screen, (
            255,
            255,
            255,
        ), button_2)

        screen.blit(start_game, (1560, 420))
        screen.blit(random_mode, (1540, 620))
        screen.blit(barry_logo, (300, 350))
        screen.blit(bear, (2100, 1000))

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)


class toy:
    def __init__(self, image):
        self.x = randint(0, 2300)
        self.y = randint(0, 1300)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (300, 300))


green_ball = toy('green_ball.png')
feather = toy('feather.png')


def random_game():

    # initilizing background
    pygame.init()
    logo = pygame.image.load("pawprint.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Barry's Corner")
    bg = pygame.image.load('wood.png')
    screen = pygame.display.set_mode((2500, 1300))

    # images
    # mouse = pygame.image.load('mouse.png')
    # mouse = pygame.transform.scale(mouse, (200, 200))
    # green_ball = pygame.image.load('green_ball.png')
    # green_ball = pygame.transform.scale(green_ball, (300, 300))
    # pink_ball = pygame.image.load('pink_ball.png')
    # pink_ball = pygame.transform.scale(pink_ball, (300, 300))
    # feather = pygame.image.load('feather.png')
    # feather = pygame.transform.scale(feather, (300, 300))

    # screen.blit(green_ball.image, (100, 50))
    # screen.blit(pink_ball, (400, 50))
    # screen.blit(feather, (800, 50))

    # pygame.display.flip()

    # def toy(toy_obj):
    #     screen.blit(bg, (0, 0))
    #     x_offset = randint(0, 2000)
    #     y_offset = randint(0, 1000)
    #     # x_offset = randrange(-50, 50, 25) + 15
    #     # y_offset = randrange(-50, 50, 25) + 15
    #     toy_obj.x += x_offset
    #     toy_obj.y += y_offset
    #     screen.blit(toy_obj.image, (toy_obj.x, toy_obj.y))

    orange_ball = pygame.image.load('orange_ball.png')
    orange_ball = pygame.transform.scale(orange_ball, (300, 300))
    toyX = 1000
    toyY = 650

    def toy(x, y):
        screen.blit(orange_ball, (x, y))

    running = True

    while running:

        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # toy(mouse, x, y)
        # toy(green_ball,randomx,0)
        # toy(feather,0,0)

        for i in range(10):
            number = randrange(2000)
            numberY = randrange(1200)
        toyX = number
        toyY = numberY

        if toyX <= -40:
            toyX = -40
        elif toyX >= 2225:
            toyX = 2225
        if toyY <= -20:
            toyY = -20
        elif toyY >= 1070:
            toyY = 1070

        toy(toyX, toyY)
        # toy(feather)

        # pygame.time.wait(500)
        # toy(feather, x, y)
        pygame.display.update()


if __name__ == "__main__":
    # call the main function
    main_menu()