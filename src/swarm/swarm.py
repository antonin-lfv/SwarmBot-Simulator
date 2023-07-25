from .robot import Robot


class Swarm:
    def __init__(self, swarm_type, number_of_robots):
        """
        :param swarm_type: Define the type of swarm
        :param number_of_robots: integer that define the number of robots in the swarm
        """
        self.swarm_type = swarm_type
        self.number_of_robots = number_of_robots
        self.robots = self.create_robots()

    def create_robots(self):
        robots = []
        for i in range(self.number_of_robots):
            name = f"Robot_{i}"
            robots.append(Robot(name=name))
        return robots

    def move(self, map_object):
        for robot in self.robots:
            if self.swarm_type == "Random_swarm":
                robot.move(map_object)

    def get_positions(self):
        return [robot.position for robot in self.robots]

    def get_velocities(self):
        return [robot.velocity for robot in self.robots]

    def get_names(self):
        return [robot.name for robot in self.robots]

    def get_robots(self):
        return self.robots
