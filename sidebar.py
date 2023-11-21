import streamlit as st
import pandas as pd

# Caching
@st.cache_data
# @st.cache(allow_output_mutation=True)
def get_data_from_excel():
    df = pd.read_excel(r'titanic.xlsx')
    return df

# Creating Sidebar filters
class Sidebar:

    def __init__(self):
        self.df = get_data_from_excel()
        self.df["ticket"] = self.df["class"]
        self.df_selection = None
        self.header = st.sidebar.header("Please Filter Here:")
        self.gender = st.sidebar.multiselect(
            "Select the Gender:",
            options = self.df["sex"].unique(),
            default = self.df["sex"].unique(),
            key='gender'
        )
        self.ticket = st.sidebar.multiselect(
            "Select the Class:",
            options = self.df["ticket"].unique(),
            default = self.df["ticket"].unique(),
            key='ticket'
        )
        self.excursion = st.sidebar.multiselect(
            "Select the Excursion:",
            options = self.df["went_excursion"].unique(),
            default = self.df["went_excursion"].unique(),
            key='excursion'
        )

    def select(self):
        self.df_selection = self.df.query(
            "sex == @self.gender & went_excursion == @self.excursion & ticket == @self.ticket"
        )
        # Creating Metrics/KPI's
        total_passengers = self.df_selection["name"].count()
        average_age = round(self.df_selection["age"].mean(), 1)
        total_excursions = self.df_selection["went_excursion"].sum()
        left_column, middle_column, right_column = st.columns(3)
        with left_column:
            st.subheader("Total Passengers:")
            st.subheader(f"{total_passengers}")
        with middle_column:
            st.subheader("Average Age:")
            st.subheader(f"{average_age}")
        with right_column:
            st.subheader("Total Excursions:")
            st.subheader(f"{total_excursions}")

        st.markdown("---")
    
    

            

