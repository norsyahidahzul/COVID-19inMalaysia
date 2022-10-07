import streamlit as st

st.set_page_config(
    page_title="Interactive Dashboard_COVID-19 in Malaysia",
    page_icon="🦠")
	
st.write("# Welcome to Interactive Dashboard of COVID-19 in Malaysia! 👋")


st.markdown(
    """
    This interactive dashboard of COVID-19 in Malaysia is made for research purpose of Master's degree. This dashboard
    contains COVID-19 simulator, COVID-19 predictor and Overview of COVID-19 cases in Malaysia. This dashboard is mainly
    builded for researcher, analyst and government agency to help making a proper decision upon the spike or subside of COVID-19 cases.
	
👈 **Click the pages on the sidebar** to explore this interactive dashboard!

Thank you.
"""
)

import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

st.button("Re-run")
