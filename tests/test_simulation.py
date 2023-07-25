from src.map.map import Map
from src.swarm.robot import Robot

r = Robot("Robot_1", (2, 35), "up_left", 5)
my_map = Map("Empty_map")
my_map.plot_map()

r.move(my_map)
print(r.get_position())
print(r.get_path())
