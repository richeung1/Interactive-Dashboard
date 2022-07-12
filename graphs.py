import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sidebar import Sidebar
import plotly_express as px
import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = 'browser'

class Visualizer:

    def __init__(self):
        self.sidebar = Sidebar()
        self.sidebar.select()
    
    def male_v_female(self):
        self.malevsfemale = (
            self.sidebar.df_selection.groupby(by=["sex"]).count()["name"]
        )
        figure = px.bar(
            self.malevsfemale,
            title='Male vs Female',
            x = self.malevsfemale.index,
            y = "name",
            orientation = "v",
            color_discrete_sequence=["#0083B8"] * len(self.malevsfemale),
            template="plotly_white",
            labels={
                'name':'Frequency',
                'sex': 'Sex'
            }
        )
        figure.update_layout(title_x=0.5)
        return figure

    def passengers(self):
        self.passenger_by_class = (self.sidebar.df_selection[['ticket', 'went_excursion']])
        self.passenger_by_class['went_excursion'] = self.passenger_by_class['went_excursion'].replace([0, 1], ['No', 'Yes'])
        crosstab= pd.crosstab(self.passenger_by_class['ticket'], self.passenger_by_class['went_excursion'])
        # st.write(crosstab)

        data = []
        for x in crosstab.columns:
            data.append(go.Bar(name=str(x), x=crosstab.index, y=crosstab[x]))

        figure = go.Figure(data)
        figure.update_layout(
                        title={'text': 'Passenger Class vs Excursion',
                               'x': 0.5,
                               'y': 0.9,
                               'xanchor': 'center',
                               'yanchor': 'top'},
                        barmode='group',
                        xaxis_title='Passenger Class',
                        yaxis_title='Frequency'
        )
        return figure
    
    def visualize(self):
        left_column, right_column = st.columns(2)
        fig_male_female = self.male_v_female()
        fig_passenger_class = self.passengers()
        left_column.plotly_chart(fig_male_female, use_container_width=True)
        right_column.plotly_chart(fig_passenger_class, use_container_width=True)