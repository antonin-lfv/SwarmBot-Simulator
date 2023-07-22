import time
import arcade
import arcade.gui
import random

SPRITE_SCALING = 1 / 16
SPRITE_SIZE = int(128 * SPRITE_SCALING)
SEMISPRITE_SIZE = int(SPRITE_SIZE / 2)

MAP_WIDTH = 832
MAP_HEIGHT = 800
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
SCREEN_TITLE = "SwarmBot Simulator"

ROBOT_SPEED = 1
NUMBER_OF_ROBOTS = 30


class SecondPage(arcade.View):
    """ Main application class. """

    def __init__(self, width):
        """
        Initializer
        """
        super().__init__(width)

        # Sprite lists
        self.robot_list = None
        self.wall_list = None
        self.target_list = None
        self.number_of_robots = NUMBER_OF_ROBOTS
        self.setup()

    def on_show(self):
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.wall_list = arcade.SpriteList()
        self.robot_list = arcade.SpriteList()
        self.target_list = arcade.SpriteList()

        # -- Set up the walls

        # Create horizontal rows of boxes
        for x in range(SEMISPRITE_SIZE, MAP_WIDTH, SPRITE_SIZE):
            # Bottom edge
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = SEMISPRITE_SIZE
            self.wall_list.append(wall)

            # Top edge
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = MAP_HEIGHT - SEMISPRITE_SIZE
            self.wall_list.append(wall)

        # Create vertical columns of boxes
        for y in range(SEMISPRITE_SIZE * 3, MAP_HEIGHT, SPRITE_SIZE):
            # Left
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = SEMISPRITE_SIZE
            wall.center_y = y
            self.wall_list.append(wall)

            # Right
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = MAP_WIDTH - SEMISPRITE_SIZE
            wall.center_y = y
            self.wall_list.append(wall)

        # -- Set up the robots

        # Create robots
        for i in range(self.number_of_robots):
            robot = arcade.Sprite(":resources:images/space_shooter/playerShip3_orange.png", 0.15)
            robot.center_x = random.randrange(100, 700)
            robot.center_y = random.randrange(100, 500)
            while robot.change_x == 0 and robot.change_y == 0:
                robot.change_x = ROBOT_SPEED
                robot.change_y = ROBOT_SPEED

            self.robot_list.append(robot)

        # -- Set up the target

        # Place the target on a random spot if it is not already on a wall
        target = arcade.Sprite(":resources:images/items/coinGold.png", 0.25)
        target.center_x = random.randrange(SPRITE_SIZE, MAP_WIDTH - SPRITE_SIZE)
        target.center_y = random.randrange(SPRITE_SIZE, MAP_HEIGHT - SPRITE_SIZE)

        self.target_list = target

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        # Draw all the sprites.
        self.wall_list.draw()
        self.robot_list.draw()
        self.target_list.draw()

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Get the time of the beginning of the update
        start_time = time.time()

        for robot in self.robot_list:

            # -- collision with walls
            robot.center_x += robot.change_x
            walls_hit = arcade.check_for_collision_with_list(robot, self.wall_list)
            for wall in walls_hit:
                if robot.change_x > 0:
                    robot.right = wall.left
                elif robot.change_x < 0:
                    robot.left = wall.right
            if len(walls_hit) > 0:
                robot.change_x *= -1

            robot.center_y += robot.change_y
            walls_hit = arcade.check_for_collision_with_list(robot, self.wall_list)
            for wall in walls_hit:
                if robot.change_y > 0:
                    robot.top = wall.bottom
                elif robot.change_y < 0:
                    robot.bottom = wall.top
            if len(walls_hit) > 0:
                robot.change_y *= -1

            # Add a random chance to change direction if not next to a wall
            if random.randrange(100) == 0 and len(walls_hit) == 0:
                robot.change_x *= random.choice([-1, 1])
                robot.change_y *= random.choice([-1, 1])

            # Check if robot has reached the target
            if arcade.check_for_collision(robot, self.target_list):
                # Get the time of the end of the update
                end_time = time.time()
                # Stop all robots and display a message in a window
                for r in self.robot_list:
                    r.change_x = 0
                    r.change_y = 0
                # Show the duration of the update in a window
                arcade.draw_text(f"Time: {end_time - start_time:.2f} seconds",
                                 50, 50, arcade.color.YELLOW, 20)


class MainView(arcade.View):
    def __init__(self, window: arcade.Window):
        super().__init__(window)
        self.window = window
        self.v_box = None
        self.manager = None

    def on_show_view(self):
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout()

        ui_text_label = arcade.gui.UITextArea(text="SwarmBot Simulator",
                                              width=450,
                                              height=40,
                                              font_size=22,
                                              font_name="Kenney Future")
        self.v_box.add(ui_text_label.with_space_around(bottom=0))

        text = "This application is a simulation of a swarm of robots. " \
               "The aim of the simulation is to show how a swarm of robots " \
               "can be used to reach a target. "
        ui_text_label = arcade.gui.UITextArea(text=text,
                                              width=450,
                                              height=60,
                                              font_size=12,
                                              font_name="Arial")
        self.v_box.add(ui_text_label.with_space_around(bottom=0))

        ui_flatbutton = arcade.gui.UIFlatButton(text="Start", width=200)
        self.v_box.add(ui_flatbutton.with_space_around(bottom=20))

        @ui_flatbutton.event("on_click")
        def on_click_flatbutton(event):
            self.manager.disable()
            self.window.show_view(SecondPage(self.window))

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_hide_view(self):
        self.manager.disable()

    def on_draw(self):
        arcade.start_render()
        self.manager.draw()


def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, SCREEN_TITLE)
    window.show_view(MainView(window))
    arcade.run()


if __name__ == "__main__":
    main()
