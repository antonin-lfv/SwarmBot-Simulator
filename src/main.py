import time

import streamlit as st

from config import Streamlit_config
from map.map import Map
from swarm.swarm import Swarm

# -- Streamlit configuration
st.set_page_config(**Streamlit_config.page_config)
st.markdown(Streamlit_config.CSS, unsafe_allow_html=True)

# -- Main title
st.markdown('<p class="first_titre">SwarmBot Simulator</p>', unsafe_allow_html=True)
st.markdown("###")

# -- Layout map and parameters
col_map, _, col_params = st.columns((0.6, 0.05, 0.35))
map_space = col_map.empty()

# Parameters
map_selector = col_params.selectbox("Map", ["Empty_map", "Random_map", "Planet_map"])
policy_selector = col_params.selectbox("Policy", ["Random_policy"])
number_of_robots_slider = col_params.number_input("Number of robots", min_value=1, max_value=50, value=1, step=1)
swarm_type_selector = col_params.selectbox("Swarm type", ["Random_swarm"])
col_params.divider()
start_simulation_button = col_params.button("Start simulation")

# -- Manage parameters
# Map
my_map = Map(map_selector)

# Policy

# Swarm
my_swarm = Swarm(swarm_type_selector, number_of_robots_slider)
my_map.set_up_swarm(my_swarm)

# Display map
map_space.plotly_chart(my_map.get_plot_map(), use_container_width=True, config={"displayModeBar": False})

# Start simulation
if start_simulation_button:
    st.toast("Simulation started !")
    for _ in range(100):
        my_map.move_swarm()
        map_space.plotly_chart(my_map.get_plot_map(), use_container_width=True, config={"displayModeBar": False})
        # sleep for 1 second
        time.sleep(0.2)

my_swarm.get_paths()

st.write("###")
st.divider()

st.markdown('<p class="section">Results</p>', unsafe_allow_html=True)

_, mid1, mid2, _ = st.columns((0.1, 0.4, 0.4, 0.1))
mid1.subheader(f"Number of robots: `{number_of_robots_slider}`")
mid1.subheader(f"Map: `{map_selector}`")
mid2.subheader(f"Policy: `{policy_selector}`")
mid2.subheader(f"Swarm type: `{swarm_type_selector}`")

st.write(my_map.get_map())
