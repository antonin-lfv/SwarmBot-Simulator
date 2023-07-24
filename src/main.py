import streamlit as st
from config import Streamlit_config
from map.map import Map

# -- Streamlit configuration
st.set_page_config(**Streamlit_config.page_config)
st.markdown(Streamlit_config.CSS, unsafe_allow_html=True)

# -- Main title
st.markdown('<p class="first_titre">SwarmBot Simulator</p>', unsafe_allow_html=True)
st.markdown("###")

# -- Layout map and parameters
col_map, _, col_params = st.columns((0.7, 0.05, 0.25))

# Map
my_map = Map("Empty_map")
map_to_plot = my_map.get_plot_map()
col_map.plotly_chart(map_to_plot, use_container_width=True, config={"displayModeBar": False})

# Parameters
map_selector = col_params.selectbox("Map", ["Empty_map", "Random_map", "Planet_map"])
policy_selector = col_params.selectbox("Policy", ["Random_policy"])
number_of_robots_slider = col_params.number_input("Number of robots", min_value=1, max_value=50, value=10, step=1)
swarm_type_selector = col_params.selectbox("Swarm type", ["Random_swarm"])
col_params.divider()
start_simulation_button = col_params.button("Start simulation")

st.write("###")
st.divider()

st.markdown('<p class="section">Results</p>', unsafe_allow_html=True)

_, mid1, mid2, _ = st.columns((0.1, 0.4, 0.4, 0.1))
mid1.subheader(f"Number of robots: `{number_of_robots_slider}`")
mid1.subheader(f"Map: `{map_selector}`")
mid2.subheader(f"Policy: `{policy_selector}`")
mid2.subheader(f"Swarm type: `{swarm_type_selector}`")
