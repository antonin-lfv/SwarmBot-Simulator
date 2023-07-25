import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot


def generateDiscreteColourScale(colour_set):
    # colour set is a list of lists
    colour_output = []
    num_colours = len(colour_set)
    divisions = 1. / num_colours
    c_index = 0.
    # Loop over the colour set
    for cset in colour_set:
        num_subs = len(cset)
        sub_divisions = divisions / num_subs
        # Loop over the sub colours in this set
        for subcset in cset:
            colour_output.append((c_index, subcset))
            colour_output.append((c_index + sub_divisions -
                                  .001, subcset))
            c_index = c_index + sub_divisions
    colour_output[-1] = (1, colour_output[-1][1])
    return colour_output


class Map:
    """
    This class is used to create a map, that will be used by the simulation.
    There are different types of maps:
    - Empty map
    - Random map
    - Planet map
    """

    def __init__(self, map_type, size=(100, 200)):
        """
        This function is used to initialize the map.
        :param map_type: The type of map to create.
        :param size: The size of the map.
        """
        self.map_type = map_type
        self.size = size
        self.map = np.zeros(size)
        self.swarm = None
        self.colors = ["#1E8449", "#D38730", "#FBFF09"]
        self.create_map()

    def create_map(self):
        """
        This function is used to create the map, by adding obstacles.
        :return: The map.
        """
        if self.map_type == "Empty_map":
            # Define borders to 1
            self.map[0, :] = 1  # First line
            self.map[:, 0] = 1  # First column
            self.map[-1, :] = 1  # Last line
            self.map[:, -1] = 1  # Last column
            # Add a random 0 value to 2, that will be the target
            self.map[np.random.randint(1, self.size[0] - 1), np.random.randint(1, self.size[1] - 1)] = 2
        elif self.map_type == "Random_map":
            raise NotImplementedError
        elif self.map_type == "Planet_map":
            raise NotImplementedError
        return self.map

    def get_map(self):
        """
        This function is used to get the map.
        :return: The map.
        """
        return self.map

    def get_plot_map(self):
        """
        This function is used to get the plot of the map.
        :return: The plot of the map.
        """
        colorscale = generateDiscreteColourScale([self.colors])
        fig = go.Figure(data=go.Heatmap(
            z=self.map,
            colorscale=colorscale,
            showscale=False))
        fig.update_yaxes(autorange="reversed", visible=False)
        fig.update_xaxes(visible=False)
        fig.update_layout(
            autosize=False,
            xaxis=dict(scaleanchor="y", scaleratio=1),
            yaxis=dict(scaleanchor="x", scaleratio=1),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=0, r=0, t=0, b=0),
        )
        return fig

    def get_size(self):
        """
        This function is used to get the size of the map.
        :return: The size of the map.
        """
        return self.size

    def get_map_type(self):
        """
        This function is used to get the type of the map.
        :return: The type of the map.
        """
        return self.map_type

    def plot_map(self):
        """
        This function is used to plot the map.
        :return: The plot of the map.
        """
        fig = self.get_plot_map()
        plot(fig, filename='map.html')

    def set_up_swarm(self, swarm):
        """
        This function is used to set up the swarm.
        :param swarm: The swarm to set up.
        """
        # TODO
        self.swarm = swarm

    def is_position_valid(self, position):
        """
        This function is used to check if a position is valid.
        :param position: The position to check as a tuple (x, y).
        :return: True if the position is valid, False otherwise.
        """
        x, y = position

        # Check if we are inside the map and not on an obstacle
        if 0 <= x < self.size[0] and 0 <= y < self.size[1] and self.map[x, y] != 1:
            return True

        return False


if __name__ == "__main__":
    my_map = Map("Empty_map")
    my_map.plot_map()
