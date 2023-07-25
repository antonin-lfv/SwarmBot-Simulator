class Robot_config:
    # Map directions to coordinate changes
    directions = {
        "up": (0, -1),
        "up_right": (1, -1),
        "right": (1, 0),
        "down_right": (1, 1),
        "down": (0, 1),
        "down_left": (-1, 1),
        "left": (-1, 0),
        "up_left": (-1, -1),
    }


class Robot:
    def __init__(self, name, position=None, direction=None, velocity=4, robot_type="Random_robot"):
        """
        :param name: the name of the robot
        :param position: the position of the robot as a tuple (x, y)
        :param direction: the direction of the robot : up, up_right, right, down_right, down, down_left, left, up_left
        :param velocity: the velocity of the robot
        :param robot_type: the type of the robot among ["Random_robot", ...]
        """
        self.name = name
        self.position = position
        self.direction = direction
        self.velocity = velocity
        self.robot_type = robot_type
        self.path = []

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def get_direction(self):
        return self.direction

    def get_velocity(self):
        return self.velocity

    def get_robot_type(self):
        return self.robot_type

    def get_path(self):
        return self.path

    def move(self, map_object):
        """
        Move the robot according to the direction, the velocity and the map
        :param map_object: Map object
        :return: last_position, path
        """

        # Map directions to coordinate changes
        directions = Robot_config.directions

        x, y = self.position
        dx, dy = directions[self.direction]
        path = [(x, y)]  # Start path with current position

        for _ in range(self.velocity):
            if map_object.is_position_valid((x + dx, y + dy)):
                x, y = x + dx, y + dy  # Move to new position
            else:
                # if we are in a corner
                if not map_object.is_position_valid((x + dx, y)) and not map_object.is_position_valid((x, y + dy)):
                    # go to opposite direction
                    dx, dy = -dx, -dy
                    if map_object.is_position_valid((x + dx, y + dy)):  # check if the opposite direction is valid
                        x, y = x + dx, y + dy
                        self.direction = list(directions.keys())[list(directions.values()).index((dx, dy))]
                else:
                    # "Bounce" off wall by reversing x or y direction depending on the current direction
                    dx, dy = (dx, -dy) if self.direction in ["up_right", "right", "down_right"] else (-dx, dy)

                    if map_object.is_position_valid((x + dx, y + dy)):  # check if the bounced direction is valid
                        x, y = x + dx, y + dy
                        self.direction = list(directions.keys())[list(directions.values()).index((dx, dy))]

            path.append((x, y))  # Add new position to path

        self.path.extend(path)  # Add path to robot's path
        self.position = x, y  # Update robot's position
