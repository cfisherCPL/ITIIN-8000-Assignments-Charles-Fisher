import random
import time
import threading
import pygame
import os
from random import randrange
pygame.font.init()


# Create our Main Surface
WIDTH, HEIGHT = 1200, 800  # Define Width and Height as a Tuple
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the surface
pygame.display.set_caption("Play Tag!")  # Label the window with game name

HUD_FONT = pygame.font.SysFont('arial', 50)

# Color Pallette
GRASS_GREEN = (50, 175, 60)
WHITE = (255, 255, 255)

# Define
FPS = 60

# Sprites
SPRITE_WIDTH = 32
SPRITE_HEIGHT = 32
DEER_SPRITE = pygame.image.load(os.path.join('Assets', 'ham.png'))
DEER = pygame.transform.scale(DEER_SPRITE, (SPRITE_WIDTH, SPRITE_HEIGHT))

WOLF_SPRITE = pygame.image.load(os.path.join('Assets', 'wolf.png'))
WOLF = pygame.transform.scale(WOLF_SPRITE, (SPRITE_WIDTH, SPRITE_HEIGHT))

# RANDOM START POSITIONS
DEER_STARTX = random.randint(5,(WIDTH / 2)) # random start on left half of screen
DEER_STARTY = random.randint(5,HEIGHT)

WOLF_STARTX = random.randint((WIDTH/2),(WIDTH-5))
WOLF_STARTY = random.randint(5,HEIGHT)

# PASSABLE IT STATUS?
it_status = random.randint(1, 2)

timer_thing = 0

def update_timer():
    global timer_thing
    x = 0
    while x < 5:
        timer_thing += 1
        time.sleep(1)
        x += 1
    if timer_thing == 5:
        timer_thing = 0


def get_it():
    return it_status

def set_it(new_status):
    global it_status
    it_status = new_status

def who_is_it():
    wolfit = 'Wolf is it!'
    deerit = 'Deer is it!'
    if it_status == 1:
        return wolfit
    elif it_status == 2:
        return deerit

# User Events
CAUGHT = pygame.USEREVENT + 1  # the plus segment adds to the event queue
# if adding more you use a higher number to the queue, +2 and soforth

# Game Parameters
SPEED = 5  # what gets added to the position of a sprite when key is pressed


# Define a main function that runs the game
def main():
    # Create hit boxes
    deer = pygame.Rect(DEER_STARTX, DEER_STARTY, SPRITE_WIDTH, SPRITE_HEIGHT) # this is where we can plug in random starts!
    wolf = pygame.Rect(WOLF_STARTX, WOLF_STARTY, SPRITE_WIDTH, SPRITE_HEIGHT)

    clock = pygame.time.Clock() # this creates a clock that keeps track of run and framerate
    run = True  # set run to True
    # While loop that runs the game
    while run:  # Game Loop

        clock.tick(FPS) # uses the defined FPS value to tick the loop along
        for event in pygame.event.get():  # Checks for EVENTS
            if event.type == pygame.QUIT:  # if close clicked
                run = False  # change run to False to break loop

            """
            if event.type == CAUGHT:
                global it_status
                if get_it() == 1:
                    set_it(2)
                elif get_it() == 2:
                    set_it(1)
            """

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and deer.x - SPEED > 0:  # Deer Left...the and statement prevents leaving the edge of the screen
            deer.x -= SPEED
        if keys_pressed[pygame.K_d] and deer.x + SPEED + SPRITE_WIDTH < 1200:  # Deer Right
            deer.x += SPEED
        if keys_pressed[pygame.K_w] and deer.y - SPEED > 0:  # Deer Up
            deer.y -= SPEED
        if keys_pressed[pygame.K_s] and deer.y + SPEED + SPRITE_HEIGHT < 800:  # Deer Down
            deer.y += SPEED

        if keys_pressed[pygame.K_LEFT] and wolf.x - SPEED > 0:  # Wolf Left
            wolf.x -= SPEED
        if keys_pressed[pygame.K_RIGHT] and wolf.x + SPEED + SPRITE_WIDTH < 1200:  # Wolf Right
            wolf.x += SPEED
        if keys_pressed[pygame.K_UP] and wolf.y - SPEED > 0:  # Wolf Up
            wolf.y -= SPEED
        if keys_pressed[pygame.K_DOWN] and wolf.y + SPEED + SPRITE_HEIGHT < 800:  # Wolf Down
            wolf.y += SPEED
        draw_window(deer, wolf)  # This function draws the screen
        deer_tagged(deer, wolf)  # Check if tagged

    pygame.quit()  # will close game


# Draw Window Function
def draw_window(deer, wolf):
    WIN.fill(GRASS_GREEN)  # Draw the Grass
    WIN.blit(DEER, (deer.x, deer.y))  # Sprites
    WIN.blit(WOLF, (wolf.x, wolf.y))  # Sprites

    # make sure this is BEFORE your update, 5 head
    it_status_display = HUD_FONT.render(
        '' + str(who_is_it()), 1, WHITE)
    WIN.blit(it_status_display, (10, 10))

    timer_status = HUD_FONT.render(
        'No Tag Back: ' + str(timer_thing), 1, WHITE)
    WIN.blit(timer_status, (WIDTH - timer_status.get_width() -10, 10))

    pygame.display.update()  # Update the screen





# Create a function to determine if tagged
def deer_tagged(deer, wolf):
    if deer.colliderect(wolf):
        # pygame.event.post(pygame.event.Event(CAUGHT))
        global it_status
        if timer_thing == 0:
            if get_it() == 1:
                it_status = 2
            elif get_it() == 2:
                it_status = 1
            t = threading.Thread(target=update_timer)
            t.start()


if __name__ == "__main__":
    main()