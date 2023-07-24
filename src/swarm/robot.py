class Robot:
    def __init__(self, name, position, direction, velocity=4, robot_type="Random_robot"):
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

    def move(self, map_object):
        """
        Move the robot according to the direction, the velocity and the map
        :return:
        """
        # TODO
        ...
