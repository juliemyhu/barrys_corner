""" pygame """
import pygame
""" main loop for Barrys Corner"""

# toy


# define a main function
def main():

    # initialize the pygame module
    pygame.init()

    # load and set the logo
    logo = pygame.image.load("pawprint.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Barry's Corner")

    bg = pygame.image.load('wood.png')

    # images
    # mouse = pygame.image.load('mouse.png')
    # mouse = pygame.transform.scale(mouse, (200, 200))

    # green_ball = pygame.image.load('green_ball.png')
    # green_ball = pygame.transform.scale(green_ball, (300, 300))
    # pink_ball = pygame.image.load('pink_ball.png')
    # pink_ball = pygame.transform.scale(pink_ball, (300, 300))
    # feather = pygame.image.load('feather.png')
    # feather = pygame.transform.scale(feather, (300, 300))

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((2500, 1300))

    # screen.blit(green_ball, (10, 50))
    # screen.blit(pink_ball, (10, 50))
    # screen.blit(feather, (20, 50))
    pygame.display.set_caption("Barry's Corner")

    # define a variable to control the main loop

    #Toy
    orange_ball = pygame.image.load('orange_ball.png')
    orange_ball = pygame.transform.scale(orange_ball, (300, 300))
    toyX = 1000
    toyY = 650
    toyX_change = 0
    toyY_change = 0

    pygame.display.flip()

    def toy(x, y):
        # screen.blit(mouse, (50, 50))
        screen.blit(orange_ball, (x, y))

    running = True

    # main loop
    while running:

        screen.blit(bg, (0, 0))

        # event handling, gets all event from the event queue
        # for x in range(100):  #animate 100 frames
        #     screen.blit(orange_ball, (400, 500))  #erase
        #     position = position.move(2, 0)  #move player
        #     screen.blit(orange_ball, (200, 400))  #draw new player
        #     pygame.display.update()  #and show it all
        #     pygame.time.delay(100)
        # toyX += 0.1
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

        toyX += toyX_change
        toyY += toyY_change

        if toyX <= -40:
            toyX = -40
        elif toyX >= 2200:
            toyX = 2200
        toy(toyX, toyY)
        pygame.display.update()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()