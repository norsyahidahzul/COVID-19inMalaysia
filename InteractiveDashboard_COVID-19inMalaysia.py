import streamlit as st

st.set_page_config(
    page_title="Interactive Dashboard_COVID-19 in Malaysia",
    page_icon="🦠")
	
st.write("# Welcome to Interactive Dashboard of COVID-19 in Malaysia! 👋")
st.title("Main Page")
st.sidebar.success("select a page above.")

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

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
