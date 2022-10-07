import streamlit as st

st.set_page_config(
    page_title="Interactive Dashboard_COVID-19 in Malaysia",
    page_icon="🦠")
	
st.write("# Welcome to Interactive Dashboard of COVID-19 in Malaysia! 👋")
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


# Contents of COVID-19inMalaysia/Pages/COVID-19_Simulator.py
import streamlit as st

st.markdown("# COVID-19 Simulator ❄️")
st.sidebar.markdown("# COVID-19 Simulator ❄️")

# Contents of COVID-19inMalaysia/Pages/COVID-19_Predictor.py
import streamlit as st

st.markdown("# COVID-19 Predictor🎉")
st.sidebar.markdown("# COVID-19 Predictor 🎉")

# Contents of COVID-19inMalaysia/Pages/OverviewofCases.py
import streamlit as st

st.markdown("# Overview of Cases🎉")
st.sidebar.markdown("# Overview of Cases 🎉")
