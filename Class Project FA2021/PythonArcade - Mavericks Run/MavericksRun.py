
import arcade
import math
import random
import time


# How long should we wait idle before doing something like switching the view?
IDLE_TIME = 30.0

# Constants for the size of the screen/window to use for the game
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "TiledGame"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
# Used  for scrolling margin camera.
VIEWPORT_MARGIN_HORZ = 600
VIEWPORT_MARGIN_VERT = 350

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# Movement speed of player, in pixels per frame
# Updates per frame for sprite animations
# Sprite animations held for project turn in 12-5-21
MOVEMENT_SPEED = 7
UPDATES_PER_FRAME = 5

# Constants used to track if the player is facing left or right
# Use later for animated sprites. 11-29-21
# Animated player sprites long-listed for class presentation 12-5-21
RIGHT_FACING = 0
LEFT_FACING = 1

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 0.45
TILE_SCALING = 2.5
COIN_SCALING = 0.5
SPRITE_PIXEL_SIZE = 16
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

# A Dict of all potential starting locations
# Key used as int to pull from rand_int later
# Store the name, x coord, and y coord
SPAWN_LOCATIONS = {
    "0": ["Bell Tower", 9515, 6970],
    "1": ["Library Parking Lot", 7745, 6677],
    "2": ["Durham Parking Lot", 8935, 7848],
    "3": ["West Faculty Lot Far", 2975, 7668],
    "4": ["West Faculty Lot Near", 4335, 5688],
    "5": ["West Garage", 1635, 4849],
    "6": ["Mav Village", 2405, 3529],
    "7": ["University Village", 6145, 5089],
    "8": ["H&K Parking Lot", 10005, 4837],
    "9": ["CPACS Faculty Lot", 11575, 5769],
    "10": ["Eppley Guest Lot", 14457, 8077],
    "11": ["NE Corner Lot", 17415, 8937],
    "12": ["ASH Side Lot", 17735, 6207],
    "13": ["East Garage", 16705, 5327],
    "14": ["BioMech Lot", 13293, 2619],
    }


# Target locations on map to be used for compass
TARGET_LOCATIONS = {
    "0": ["Library 2nd Floor", 8215, 7107],
    "1": ["Biomechanics - West Entry", 13465, 2476],
    "2": ["Milo Bail Student Center", 12655, 7107],
    "3": ["CPACS - North Door", 11115, 6829],
    "4": ["Allwine Hall - West Door", 12265, 6529],
    "5": ["Strauss PAC - Main Entry", 10585, 7359],
    "6": ["Weber Fine Arts - North Entry", 6523, 7029],
    "7": ["Durham Science - South Entry", 5503, 7387],
    "8": ["Sculpture and Ceramic Studio", 9055, 4879],
    }

# Layer Names from our TileMap
LAYER_NAME_BOUNDS = "Buildings"
LAYER_NAME_FOREGROUND = "ForeGround"

# MiniMap and Constants deprecated for performance 12-5-21
"""
# Constants for MiniMap
# Background color must include an alpha component
# Default values 256, 256, 2048, 2048
MINIMAP_BACKGROUND_COLOR = arcade.get_four_byte_color(arcade.color.ALMOND)
MINIMAP_WIDTH = 400
MINIMAP_HEIGHT = 220
MAP_WIDTH = 18000
MAP_HEIGHT = 10000
"""

# TitleView used as main entry screen
class TitleView(arcade.View):

    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

        self.title_timer = 0.0
        self.music_playing = False
        self.title_music = arcade.load_sound("SoundAssets/Bit Bit Loop.mp3")
        self.title_play_music = None
        self.texture = arcade.load_texture("VisualAssets/Mavs Run 1200x720 ScreenMaker.png")

    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.BLACK)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width, 0, self.window.height)


    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)
        # arcade.draw_text("Maverick's Run", self.window.width / 2, self.window.height / 2,
        #                 arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("PRESS ANY BUTTON TO PLAY", self.window.width / 2, self.window.height / 2 - 75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        """ If the user presses any button, start the game. """
        load_screen = LoadScreen(self.game_view)
        arcade.stop_sound(self.title_play_music)
        self.window.show_view(load_screen)

    def on_update(self, delta_time: float):
        self.title_timer += delta_time
        if not self.music_playing:
            self.title_play_music = arcade.play_sound(self.title_music)
            self.music_playing = True
        if self.title_timer >= IDLE_TIME:
            load_screen = LoadScreen(self.game_view)
            arcade.stop_sound(self.title_play_music)
            self.window.show_view(load_screen)

# LoadScreen showcases a simple how-to
class LoadScreen(arcade.View):

    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        self.load_timeout = 0.0
        self.texture = arcade.load_texture("VisualAssets/MavsRun_HowTo.png")

    def on_show_view(self):
        # using same setup as above, but covering up the load time of GameView
        arcade.set_background_color(arcade.csscolor.BLACK)
        # arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_key_press(self, symbol: int, modifiers: int):
        self.game_view.new_player_start()
        self.window.show_view(self.game_view)

    def on_update(self, delta_time: float):
        self.load_timeout += delta_time
        if self.load_timeout >= IDLE_TIME:
            self.game_view.new_player_start()
            self.window.show_view(self.game_view)

# GameOver used when player arrives at location
class GameOver(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        self.game_over_timeout = 0.0

    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.FIREBRICK)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        n_ln = '\n'
        arcade.draw_text(f"You went from {self.game_view.spawn_location}",
                         self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, font_size=40, anchor_x="center")
        arcade.draw_text(f"to {self.game_view.target_name}",
                         self.window.width / 2, self.window.height / 2 - 50,
                         arcade.color.WHITE, font_size=40, anchor_x="center")
        arcade.draw_text(f"Total Time: {self.game_view.output}",
                         self.window.width / 2, self.window.height / 2 - 100,
                         arcade.color.WHITE, font_size=30, anchor_x="center")
        # Prompt for restart
        arcade.draw_text("Press R to respawn or Q to exit.", self.window.width / 2,
                         self.window.height / 2 - 150,
                         arcade.color.WHITE, font_size=25, anchor_x="center")

    def on_key_press(self, key, modifiers):
        """ If the user presses any button, start the game. """
        if key == arcade.key.Q:
            title_screen = TitleView(self.game_view)
            arcade.stop_sound(self.game_view.music_player)
            self.game_view.music_playing = False
            time.sleep(3)
            self.window.show_view(title_screen)
        elif key == arcade.key.R:
            self.game_view.new_player_start()
            self.window.show_view(self.game_view)

    def on_update(self, delta_time: float):
        self.game_over_timeout += delta_time

        if self.game_over_timeout >= IDLE_TIME:
            title_screen = TitleView(self.game_view)
            arcade.stop_sound(self.game_view.music_player)
            self.game_view.music_playing = False
            self.window.show_view(title_screen)

# GameView is the main gameplay screen and functions
class GameView(arcade.View):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        # super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE,)
        # above was prior window version vs now using views
        super().__init__()

        # Our TileMap Object
        self.tile_map = None

        # Our Scene Object
        # This badboi holds the spritelists, so take note.
        # You'll need to call the scene if you want the lists.
        self.scene = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # New variable to hold compass sprite
        self.arrow_sprite = None

        # Our physics engine
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # A Camera that can be used for scrolling the screen
        self.camera = None

        # Load sounds
        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.main_music = arcade.load_sound("SoundAssets/HinaCC0_011_Fallen_leaves.mp3")

        # A Camera that can be used to draw GUI elements
        self.gui_camera = None

        # Create a timer to show on-screen
        self.total_time = 0.0
        self.output = "00:00:00"

        # Used in scrolling
        self.view_bottom = 0
        self.view_left = 0

        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Mini-map inits.
        """
        # List of all our minimaps (there's just one)
        self.minimap_sprite_list = None
        # Texture and associated sprite to render our minimap to
        self.minimap_texture = None
        self.minimap_sprite = None
        """

        # Location storage for position ID
        self.location = None

        # Prep the location name to show on gui
        self.target_locale =None

        # Don't show the mouse cursor
        self.window.set_mouse_visible(False)

        # Spawn and target location names and x,y
        self.spawn_location = None
        self.player_start_x = None
        self.player_start_y = None
        self.target_x = None
        self.target_y = None
        self.target_name = None

        self.coin = None

        # Create a count-up timer to track idle
        self.timeout_count = 0.0

        # Track if music is playing or not
        self.music_playing = False
        self.music_player = None

        # Add objects for HUD texture items
        self.pause_hud = arcade.load_texture("VisualAssets/PauseHUD.png")
        self.move_hud = arcade.load_texture("VisualAssets/MavsRun MoveHUD.png")

        arcade.set_background_color(arcade.csscolor.GREEN)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        # Setup the Camera
        self.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Setup the GUI Camera
        self.gui_camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Name of map file to load
        map_name = "TiledMap/16px Test2.json"

        # Layer specific options are defined based on Layer names in a dictionary
        # Doing this will make the SpriteList for the platforms layer
        # use spatial hashing for detection.
        layer_options = {
            LAYER_NAME_BOUNDS: {
                "use_spatial_hash": True,
            },
        }
        # Generate randomized start and target locations
        self.random_spawn_and_target()

        # Read in the tiled map
        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)

        # Initialize Scene with our TileMap, this will automatically add all layers
        # from the map as SpriteLists in the scene in the proper order.
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # Create the Sprite lists
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Coins")



        # Add Player Spritelist before "Foreground" layer. This will make the foreground
        # be drawn after the player, making it appear to be in front of the Player.
        # Setting before using scene.add_sprite allows us to define where the SpriteList
        # will be in the draw order. If we just use add_sprite, it will be appended to the
        # end of the order.
        self.scene.add_sprite_list_before("Player", LAYER_NAME_FOREGROUND)
        self.scene.add_sprite_list_before("Player", "Coins")
        self.scene.add_sprite_list_after("Arrow", "BuildingDressing")
        self.scene.add_sprite_list_after("Player", "BuildingDressing")
        self.scene.add_sprite_list_before("Arrow", "Player")

        # Set up the player, specifically placing it at these coordinates.
        image_source = "VisualAssets/Durango_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = self.player_start_x
        self.player_sprite.center_y = self.player_start_y
        self.scene.add_sprite("Player", self.player_sprite)

        # Load the image for the target coin
        # plac initial coin
        self.coin = arcade.Sprite(":resources:images/items/gold_1.png", COIN_SCALING)
        self.coin.center_x = self.target_x
        self.coin.center_y = self.target_y
        self.scene.add_sprite("Coins", self.coin)

        self.coin2 = arcade.Sprite(":resources:images/items/coinGold.png", COIN_SCALING)
        self.coin2.center_x = 9645
        self.coin2.center_y = 6759
        self.scene.add_sprite("Coins", self.coin2)

        # Setup Initial Player Location Tracker
        # This used to not trigger until first update,
        # meaning that the first text gui draw failed.
        current_x = self.player_sprite.center_x
        current_y = self.player_sprite.center_y
        self.location = str(f"{current_x}x,{current_y}y")

        # Set up the Compass Arrow, position where the Player is
        # Draw before the player to put it under them
        arrow_source = "VisualAssets/RadialArrow.png"
        self.arrow_sprite = arcade.Sprite(arrow_source, scale= 0.6,)
        self.arrow_sprite.alpha = 128
        self.arrow_sprite.center_x = self.player_sprite.center_x
        self.arrow_sprite.center_y = self.player_sprite.center_y
        self.scene.add_sprite("Arrow", self.arrow_sprite)
        self.arrow_sprite.angle = 0

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, self.scene.get_sprite_list(LAYER_NAME_BOUNDS)
        )

        # Start the timer
        self.total_time = 0.0

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

        # Construct the minimap
        # Not anymore! 12-3-21
        """
        size = (MINIMAP_WIDTH, MINIMAP_HEIGHT)
        self.minimap_texture = arcade.Texture.create_empty(str(uuid4()), size)
        self.minimap_sprite = arcade.Sprite(center_x=MINIMAP_WIDTH / 2,
                                            center_y=SCREEN_HEIGHT - MINIMAP_HEIGHT / 2,
                                            texture=self.minimap_texture)

        self.minimap_sprite_list = arcade.scene.SpriteList()
        self.minimap_sprite_list.append(self.minimap_sprite)
        """

        # Create the target location announcement on-screen
        self.target_locale = "Go to " + self.target_name

    def random_spawn_and_target(self):
        # initialize/seed the rng
        # added to stabilize the randomizer after some crashing
        # seemed to work, but might be placebo
        random.seed()
        # Player starting position
        # X and Y are pulled from dict above
        # Random target position using same method
        rand_spawn = random.randint(0, 14)  # if more locations later, add higher second number
        rand_spawn = str(rand_spawn)
        spawn_dict_pull = SPAWN_LOCATIONS.get(rand_spawn)
        self.spawn_location = spawn_dict_pull[0]
        self.player_start_x = spawn_dict_pull[1]
        self.player_start_y = spawn_dict_pull[2]

        rand_target = random.randint(0, 8)
        rand_target = str(rand_target)
        target_dict_pull = TARGET_LOCATIONS.get(rand_target)
        self.target_name = target_dict_pull[0]
        self.target_x = target_dict_pull[1]
        self.target_y = target_dict_pull[2]


    # Minimap is cool, but blocks viewport too much
    # and wasn't helping gameplay.
    """
    def update_minimap(self):
        proj = 0, MAP_WIDTH, 0, MAP_HEIGHT
        with self.minimap_sprite_list.atlas.render_into(self.minimap_texture, projection=proj) as fbo:
            fbo.clear(MINIMAP_BACKGROUND_COLOR)
            self.scene.draw()
            # self.wall_list.draw()
            # self.player_sprite.draw()
    """

    # This should make the compass move with the player: It does!
    def update_compass(self):
        self.arrow_sprite.center_x = self.player_sprite.center_x
        # lower the draw by 28px to place at player's feer
        self.arrow_sprite.center_y = self.player_sprite.center_y - 28

        angle_temp = self.direction_lookup(self.target_x, self.arrow_sprite.center_x,
                                           self.target_y, self.arrow_sprite.center_y)

        self.arrow_sprite.angle = angle_temp + 180

    def new_player_start(self):
        # reset the timeout, if it happened
        self.timeout_count = 0.0

        # call the randomizer to get new values
        self.random_spawn_and_target()

        # Set up the target coin at coordinates
        self.coin.center_x = self.target_x
        self.coin.center_y = self.target_y
        self.coin.update()

        # Set up the player at coordinates
        self.player_sprite.center_x = self.player_start_x
        self.player_sprite.center_y = self.player_start_y
        self.target_locale = "Go to " + self.target_name
        self.total_time = 0.0

    # Direction lookup returns an angle value to be used
    # in the update of the compass sprite rotation
    def direction_lookup(self, destination_x, origin_x, destination_y, origin_y):

        delta_x = destination_x - origin_x
        delta_y = destination_y - origin_y

        # is it the 180 here making the weird flip?
        # nope. Necessary to generate a degree vs radian
        radians = math.atan2(delta_y, delta_x)

        degrees_final = math.degrees(radians)

        return degrees_final + 90

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        # Start the render. This must happen before any drawing
        # commands. We do NOT need an stop render command.
        arcade.start_render()

        # Activate our Camera
        # Don't need to do with Views? 12-3-21
        self.camera.use()

        # Draw our Scene
        self.scene.draw()

        # Update the minimap
        # Commented out 12-3-21
        # self.update_minimap()

        # Draw the minimap
        # Commented out 12-3-21
        # self.minimap_sprite_list.draw()

        # Activate the GUI camera before drawing GUI elements
        self.gui_camera.use()

        # Output the timer text.
        arcade.draw_text(self.output,
                         SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50,
                         arcade.color.WHITE, 30,
                         anchor_x="center")

        # For testing, display the player sprite current location
        arcade.draw_text(self.location,
                         SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100,
                         arcade.color.WHITE, 30,
                         anchor_x="center")

        # Display the target location name.
        arcade.draw_text(self.target_locale,
                         SCREEN_WIDTH // 2, 100,
                         arcade.color.WHITE, 30,
                         anchor_x="center")

        # Display the HUD elements for player UI help
        self.move_hud.draw_scaled(128, 72)
        self.pause_hud.draw_scaled(SCREEN_WIDTH - 128, 50, 0.65)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        self.timeout_count = 0.0

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True
        elif key == arcade.key.KEY_0:
            self.new_player_start()
        elif key == arcade.key.ESCAPE:
            # pass self, the current view, to preserve this view's state
            pause = PauseView(self)
            self.window.show_view(pause)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False

    def scroll_to_player(self):
        """
        Scroll the window to the player.
        This method will attempt to keep the player at least VIEWPORT_MARGIN
        pixels away from the edge.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """

        # --- Manage Scrolling ---

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN_HORZ
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN_HORZ
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN_VERT
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN_VERT
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom

        # Scroll to the proper location
        position = self.view_left, self.view_bottom
        self.camera.move_to(position, CAMERA_SPEED)

    def on_update(self, delta_time):
        """Movement and game logic"""
        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED

        # Call update to move the sprite
        # If using a physics engine, call update player to rely on physics engine
        # for movement, and call physics engine here.
        # Move the player with the physics engine
        self.physics_engine.update()

        # If music is not playing, start it up!
        if not self.music_playing:
            # Make sure to make a player object when you play a sound,
            # or you won't be able to stop it later
            self.music_player = arcade.play_sound(self.main_music, looping=True, volume=0.6)
            self.music_playing = True

        # Draw the timer
        self.total_time += delta_time
        # Calculate minutes
        minutes = int(self.total_time) // 60
        # Calculate seconds by using a modulus (remainder)
        seconds = int(self.total_time) % 60
        # Calculate 100s of a second
        seconds_100s = int((self.total_time - seconds) * 100)
        # Figure out our output
        self.output = f"{minutes:02d}:{seconds:02d}:{seconds_100s:02d}"

        # Draw Player location
        current_x = self.player_sprite.center_x
        current_y = self.player_sprite.center_y
        self.location = str(f"{current_x}x,{current_y}y")

        # Scroll the screen to the player
        self.scroll_to_player()

        # Rotate the compass toward the target from current location
        self.update_compass()

        # Add time to the count-up timer
        # This will get reset to zero with any keypress
        self.timeout_count += delta_time

        found_coin = arcade.check_for_collision(self.coin, self.player_sprite)
        if found_coin:
            arcade.play_sound(self.collect_coin_sound)
            self.left_pressed = False
            self.right_pressed = False
            self.up_pressed = False
            self.down_pressed = False
            game_over = GameOver(self)
            self.window.show_view(game_over)

        if self.timeout_count >= IDLE_TIME:
            title_screen = TitleView(self)
            self.window.show_view(title_screen)
            arcade.stop_sound(player=self.music_player)
            self.music_playing = False

# PauseView allows players to pause the game inside of GameView
class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

        # initialize a countdown for the pause screen itself
        self.pause_idle = 0.0

    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE)

    def on_draw(self):
        arcade.start_render()

        # Draw player, for effect, on pause screen.
        # The previous View (GameView) was passed in
        # and saved in self.game_view.
        player_sprite = self.game_view.player_sprite
        player_sprite.draw()

        # draw an orange filter over them
        arcade.draw_lrtb_rectangle_filled(left=player_sprite.left,
                                          right=player_sprite.right,
                                          top=player_sprite.top,
                                          bottom=player_sprite.bottom,
                                          color=arcade.color.ORANGE + (200,))

        arcade.draw_text("PAUSED FOR 30SEC", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

        # Show tip to return or reset
        arcade.draw_text("Press ESC to return",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 30,
                         arcade.color.BLACK,
                         font_size=25,
                         anchor_x="center")
        arcade.draw_text("Press ENTER to respawn",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 65,
                         arcade.color.BLACK,
                         font_size=25,
                         anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:   # resume game
            self.window.show_view(self.game_view)
        elif key == arcade.key.ENTER:  # reset game
            self.game_view.new_player_start()
            self.window.show_view(self.game_view)

    def on_update(self, delta_time: float):
        self.pause_idle += delta_time
        if self.pause_idle >= IDLE_TIME:
            self.window.show_view(self.game_view)


def main():
    """ Main function """

    # Draw the window to be used for the game
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    # Create a GameView object as the main game to pass to the other Views
    game_view = GameView()
    # Run setup from gameview to build map from tiled json and import sprites
    # done as part of main startup due to long load time with larger map
    game_view.setup()
    # make the titleView object
    start_view = TitleView(game_view)
    # Show the titleView screen in the window
    window.show_view(start_view)
    # start the game via the arcade library
    arcade.run()


if __name__ == "__main__":
    main()
