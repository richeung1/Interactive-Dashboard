import pandas as pd 
import streamlit as st 
import plotly_express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# Hide Streamlit Style
hide_st_style = """
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility:hidden;}
            header {visibility:hidden;}
            </style.
            """

st.markdown(hide_st_style, unsafe_allow_html=True)


@st.cache(allow_output_mutation=True)
def get_data_from_excel():
    df = pd.read_excel('titanic.xlsx')
    return df

df = get_data_from_excel()


df['ticket'] = df['class']

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")

Gender = st.sidebar.multiselect(
    "Select the Gender:",
    options = df["sex"].unique(),
    default = df["sex"].unique()
)

Ticket = st.sidebar.multiselect(
    "Select the Class:",
    options = df["ticket"].unique(),
    default = df["ticket"].unique()
)

Excursion = st.sidebar.multiselect(
    "Select the Excursion:",
    options = df["went_excursion"].unique(),
    default = df["went_excursion"].unique()
)

df_selection = df.query(
    "sex == @Gender & went_excursion == @Excursion & ticket == @Ticket"
)

# ---- MAIN PAGE ----
st.title(":bar_chart: Titanic Dashboard")
st.markdown("##")

# TOP KPI's
total_passengers = df_selection["name"].count()
average_age = round(df_selection["age"].mean(), 1)
total_excursions = df_selection["went_excursion"].sum()

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


# Graphs/Visualizations

# Class by Sex
malevsfemale = (
    df_selection.groupby(by=["sex"]).count()["name"]
)

fig_male_female = px.bar(
    malevsfemale,
    x = "name",
    y = malevsfemale.index,
    orientation = "h",
    color_discrete_sequence=["#0083B8"] * len(malevsfemale),
    template="plotly_white",
)

# st.plotly_chart(fig_male_female)


# Excursion by Class
passenger_by_class = (
    df_selection.groupby(by=["class"]).count()["name"]
)

fig_passenger_class = px.bar(
    passenger_by_class,
    x="name",
    y= passenger_by_class.index,
    orientation = "v"
)

# st.plotly_chart(fig_passenger_class)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_male_female, use_container_width=True)
right_column.plotly_chart(fig_passenger_class, use_container_width=True)

st.write(df_selection)

