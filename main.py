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
    ball = pygame.image.load('mouse.png')

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((500, 500))

    screen.blit(ball, (50, 50))

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