import pandas as pd 
import streamlit as st 
import plotly_express as px
import plotly.graph_objects as go


# @st.cache
# def get_data_from_excel():
#     return pd.read_excel("C:/Users/riche/Desktop/streamlit/titanic.xlsx")
# df = get_data_from_excel()

df = pd.read_excel("C:\\Users\\riche\\Desktop\\streamlit\\titanic.xlsx")


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
class_by_sex = (
    df_selection.groupby(by=["sex"]).count()["name"]
)

fig_class_sex = px.bar(
    class_by_sex,
    x = "name",
    y = class_by_sex.index,
    orientation = "h",
    color_discrete_sequence=["#0083B8"] * len(class_by_sex),
    template="plotly_white",
)

st.plotly_chart(fig_class_sex)


# Excursion by Class
passenger_class = ["Yes", "No"]

fig_class_age = go.Figure(data=[
    go.Bar(name = "First Class", x = passenger_class, y = [20, 14]),
    go.Bar(name = "Second Class", x = passenger_class, y = [12, 18]),
    go.Bar(name = "Third Class", x = passenger_class, y = [13, 15])
])

fig_class_age.update_layout(barmode="group")
st.plotly_chart(fig_class_age)


# left_column, right_column = st.columns(2)
# left_column.plotly_chart(fig_class_sex, use_container_width=True)
# right_column.plotly_chart(fig_class_age, use_container_width=True)

st.write(df_selection)


