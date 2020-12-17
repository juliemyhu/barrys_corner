""" pygame """
import pygame
""" main loop for Barrys Corner"""


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
    mouse = pygame.image.load('mouse.png')
    mouse = pygame.transform.scale(mouse, (200, 200))
    orange_ball = pygame.image.load('orange_ball.png')
    orange_ball = pygame.transform.scale(orange_ball, (300, 300))
    green_ball = pygame.image.load('green_ball.png')
    green_ball = pygame.transform.scale(green_ball, (300, 300))
    pink_ball = pygame.image.load('pink_ball.png')
    pink_ball = pygame.transform.scale(pink_ball, (300, 300))
    feather = pygame.image.load('feather.png')
    feather = pygame.transform.scale(feather, (300, 300))

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((2500, 1300))

    screen.blit(bg, (0, 0))
    screen.blit(mouse, (50, 50))
    screen.blit(orange_ball, (10, 50))
    screen.blit(green_ball, (10, 50))
    screen.blit(pink_ball, (10, 50))
    screen.blit(feather, (20, 50))

    pygame.display.flip()
    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()