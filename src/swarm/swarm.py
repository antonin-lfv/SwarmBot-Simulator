from .robot import Robot


class Swarm:
    def __init__(self, swarm_type, number_of_robots, map_object):
        self.swarm_type = swarm_type
        self.number_of_robots = number_of_robots
        self.map = map_object
        self.robots = self.create_robots()

    def create_robots(self):
        robots = []
        for i in range(self.number_of_robots):
            name = f"Robot_{i}"
            position = (1, 1)
            velocity = 5
            robots.append(Robot(name, position, velocity))
        return robots

    def move(self):
        for robot in self.robots:
            robot.move()
            robot.position = self.map.get_new_position(robot.position, robot.velocity)

    def get_positions(self):
        return [robot.position for robot in self.robots]

    def get_velocities(self):
        return [robot.velocity for robot in self.robots]

    def get_names(self):
        return [robot.name for robot in self.robots]

    def get_robots(self):
        return self.robots
