import streamlit as st
from multiapp import MultiApp
from apps import mainpage,COVID-19_Simulator 

app = MultiApp()

app.add_ap("Main Page",mainpage.app)
app.add_ap("COVID-19 Simulator",COVID-19_Simulator.app)
app.run()
