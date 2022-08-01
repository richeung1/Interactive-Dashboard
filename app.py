import pandas as pd 
import streamlit as st 
import plotly_express as px
import plotly.graph_objects as go
import matplotlib
import matplotlib.pyplot as plt
import base64
# import tkinter as tk
from io import StringIO, BytesIO
from sidebar import Sidebar
from graphs import Visualizer

# Formatting Streamlit layout
st.set_page_config(layout="wide")

def main(): 
    hide_st_style = """
                <style>
                #MainMenu {visibility:hidden;}
                footer {visibility:hidden;}
                header {visibility:hidden;}
                </style.
                """
    # Main page
    st.title(":bar_chart: Titanic Dashboard")
    st.markdown("##")

    # Visualizations
    visualizer = Visualizer()
    visualizer.visualize()

    # Download File Button
    st.subheader("Downloads:")

    with open(r'titanic.xlsx', 'rb') as my_file:
        st.download_button(label= "Download Data (Excel)", data = my_file, file_name = "titanic.xlsx", mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

if __name__ == '__main__':
    main()