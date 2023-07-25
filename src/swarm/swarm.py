import numpy as np

from .robot import Robot, Robot_config


class Swarm:
    def __init__(self, swarm_type, number_of_robots):
        """
        :param swarm_type: Define the type of swarm among ["Random_swarm", ...]
        :param number_of_robots: integer that define the number of robots in the swarm
        """
        self.swarm_type = swarm_type
        self.number_of_robots = number_of_robots
        self.robots = self.create_robots()

    def create_robots(self):
        robots = []
        for i in range(self.number_of_robots):
            name = f"Robot_{i}"
            r = Robot(name=name)
            if self.swarm_type == "Random_swarm":
                # set a random direction among the 8 possibilities
                r.set_direction(np.random.choice(list(Robot_config.directions.keys())))
            else:
                raise ValueError("The swarm type is not recognized.")
            robots.append(r)
        return robots

    def move(self, map_object):
        for robot in self.robots:
            robot.move(map_object)

    def get_positions(self):
        return [robot.position for robot in self.robots]

    def get_velocities(self):
        return [robot.velocity for robot in self.robots]

    def get_names(self):
        return [robot.name for robot in self.robots]

    def get_robots(self):
        return self.robots

    def get_paths(self):
        for robot in self.robots:
            print(robot.get_path(), "\n")
