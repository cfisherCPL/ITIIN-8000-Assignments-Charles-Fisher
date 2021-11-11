import random
import time
import threading
import pygame
import os


from random import randrange
file = 'Assets/Attic Secrets.mp3'
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.event.wait()

HIT_SOUND = pygame.mixer.Sound('Assets/Grenade+1.mp3')

# Create our Main Surface
WIDTH, HEIGHT = 1200, 800  # Define Width and Height as a Tuple
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the surface
pygame.display.set_caption("Play Tag!")  # Label the window with game name

HUD_FONT = pygame.font.SysFont('arial', 40)

# Color Pallette
GRASS_GREEN = (50, 175, 60)
WHITE = (255, 255, 255)
RED = (200,15,0)

# Define
FPS = 60

# Sprites
SPRITE_WIDTH = 128
SPRITE_HEIGHT = 128

DEER_FACE = 'R'
DEER_SPRITE = pygame.image.load(os.path.join('Assets', 'deer.png'))
DEER = pygame.transform.scale(DEER_SPRITE, (SPRITE_WIDTH, SPRITE_HEIGHT))
DEER_FLIP = pygame.transform.flip(DEER, True, False)

WOLF_FACE = 'R'
WOLF_SPRITE = pygame.image.load(os.path.join('Assets', 'arctic-fox.png'))
WOLF = pygame.transform.scale(WOLF_SPRITE, (SPRITE_WIDTH, SPRITE_HEIGHT))
WOLF_FLIP = pygame.transform.flip(WOLF, True, False)

# RANDOM START POSITIONS
DEER_STARTX = random.randint(5,(WIDTH / 2)) # random start on left half of screen
DEER_STARTY = random.randint(5,(HEIGHT-5) - SPRITE_HEIGHT)

WOLF_STARTX = random.randint((WIDTH/2),(WIDTH-5) - SPRITE_WIDTH)
WOLF_STARTY = random.randint(5,(HEIGHT-5) - SPRITE_HEIGHT)

# PASSABLE IT STATUS?
# starts randomly for players
it_status = random.randint(1, 2)

# to tag backsies timer countdown
timer_thing = 0
def update_timer():
    global timer_thing
    timer_thing = 3
    while timer_thing > 0:
        time.sleep(1)
        timer_thing -= 1

# tags remaining so the game can actually end
wolftags = 2
deertags = 2

# lets get a shotclock kind of thing that flips the it status every 10sec
tag_timer = 0
def tag_clock():
    global tag_timer
    global it_status
    tag_timer = 6
    while tag_timer > 0:
        time.sleep(1)
        tag_timer -= 1
    if get_it() == 1:
        it_status = 2
    elif get_it() == 2:
        it_status = 1
    tag_clock()

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
SPEED = 7  # what gets added to the position of a sprite when key is pressed


# Define a main function that runs the game
def main():
    # Create hit boxes
    deer = pygame.Rect(DEER_STARTX, DEER_STARTY, SPRITE_WIDTH, SPRITE_HEIGHT) # this is where we can plug in random starts!
    wolf = pygame.Rect(WOLF_STARTX, WOLF_STARTY, SPRITE_WIDTH, SPRITE_HEIGHT)

    clock = pygame.time.Clock() # this creates a clock that keeps track of run and framerate

    t2 = threading.Thread(target=tag_clock)
    t2.daemon = True
    t2.start()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    pygame.event.wait()
    run = True  # set run to True
    # While loop that runs the game
    while run:  # Game Loop

        clock.tick(FPS) # uses the defined FPS value to tick the loop along
        # start the shotclock timer

        for event in pygame.event.get():  # Checks for EVENTS
            if event.type == pygame.QUIT:  # if close clicked
                run = False  # change run to False to break loop


            if event.type == CAUGHT:
               HIT_SOUND.play()
        global DEER_FACE
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and deer.x - SPEED > 0:  # Deer Left...the and statement prevents leaving the edge of the screen
            deer.x -= SPEED
            DEER_FACE = 'L'
        if keys_pressed[pygame.K_d] and deer.x + SPEED + SPRITE_WIDTH < 1200:  # Deer Right
            deer.x += SPEED
            DEER_FACE = 'R'
        if keys_pressed[pygame.K_w] and deer.y - SPEED > 0:  # Deer Up
            deer.y -= SPEED
        if keys_pressed[pygame.K_s] and deer.y + SPEED + SPRITE_HEIGHT < 800:  # Deer Down
            deer.y += SPEED

        global WOLF_FACE
        if keys_pressed[pygame.K_LEFT] and wolf.x - SPEED > 0:  # Wolf Left
            wolf.x -= SPEED
            WOLF_FACE = 'L'
        if keys_pressed[pygame.K_RIGHT] and wolf.x + SPEED + SPRITE_WIDTH < 1200:  # Wolf Right
            wolf.x += SPEED
            WOLF_FACE = 'R'
        if keys_pressed[pygame.K_UP] and wolf.y - SPEED > 0:  # Wolf Up
            wolf.y -= SPEED
        if keys_pressed[pygame.K_DOWN] and wolf.y + SPEED + SPRITE_HEIGHT < 800:  # Wolf Down
            wolf.y += SPEED
        deer_tagged(deer, wolf)  # Check if tagged
        draw_window(deer, wolf)  # This function draws the screen
        if wolftags == 0:
            draw_winner("Deer Wins!")
            run = False
        elif deertags == 0:
            draw_winner("Wolf Wins!")
            run = False

    pygame.quit()  # will close game


# Draw Window Function
def draw_window(deer, wolf):
    WIN.fill(GRASS_GREEN)  # Draw the Grass

    # make sure this is BEFORE your update, 5 head
    it_status_display = HUD_FONT.render(
        '' + str(who_is_it()), 1, WHITE)
    WIN.blit(it_status_display, (10, 10))

    timer_status = HUD_FONT.render(
        'No Tag Back: ' + str(timer_thing), 1, WHITE)
    WIN.blit(timer_status, (WIDTH - timer_status.get_width() - 10, 10))

    wolftag_hud = HUD_FONT.render(
        'Wolf Lives: ' + str(wolftags), 1, WHITE)
    WIN.blit(wolftag_hud, (WIDTH - wolftag_hud.get_width() - 10, 700))

    deertag_hud = HUD_FONT.render(
        'Deer Lives: ' + str(deertags), 1, WHITE)
    WIN.blit(deertag_hud, (10, 700))

    tagtimer_hud = HUD_FONT.render(
        'Auto-It In: ' + str(tag_timer), 1, WHITE)
    WIN.blit(tagtimer_hud, (WIDTH/2 - tagtimer_hud.get_width() / 2, 650))

    if DEER_FACE == 'R':
        WIN.blit(DEER, (deer.x, deer.y))  # Sprites
    elif DEER_FACE == 'L':
        WIN.blit(DEER_FLIP, (deer.x, deer.y))

    if WOLF_FACE == 'R':
        WIN.blit(WOLF, (wolf.x, wolf.y))  # Sprites
    elif WOLF_FACE == 'L':
        WIN.blit(WOLF_FLIP, (wolf.x, wolf.y))  # Sprites
    pygame.display.update()  # Update the screen

# When one player is out of lives, display that the other has won.
def draw_winner(text):
    draw_text = HUD_FONT.render(text, 1, RED)
    WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() /
                         2,  draw_text.get_height() + 5))
    pygame.display.update()
    pygame.time.delay(5000)


# Create a function to determine if tagged
def deer_tagged(deer, wolf):
    if deer.colliderect(wolf):

        global it_status
        global deertags
        global wolftags
        global tag_timer

        if timer_thing == 0:
            pygame.event.post(pygame.event.Event(CAUGHT))
            tag_timer = 6
            if get_it() == 1:
                it_status = 2
                deertags -= 1
            elif get_it() == 2:
                it_status = 1
                wolftags -= 1
            # start the no-backsies countdown
            t = threading.Thread(target=update_timer)
            t.daemon = True
            t.start()



if __name__ == "__main__":
    main()