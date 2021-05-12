import datetime
import glob
import logging
import os

import numpy as np
import plotly.graph_objs as go
from plotly.offline import plot
import plotly.express as px

import plotly
import pandas as pd


logger = logging.getLogger(__name__)


class plot:

    def __init__(self, csv):
        self.csv = csv
        self.cols =  csv.columns[1:]


    def bar(self,c_1,c_2,c_3):
        factors = pd.concat(
            [
                self.csv[c_1]

            ]
        )
        df = pd.DataFrame({'frame': factors.value_counts()})
        print(df)

        data = go.Bar(
            x=df.index,
            y=df.frame,

        )

        layout = go.Layout(
            height=600,
            width=1000,
            margin=go.layout.Margin(l=200),
            title=c_1+"  Bar Chart")

        fig = go.Figure(data=data, layout=layout)

        plot = fig.to_html(full_html=False, default_height=500, default_width=700)

        return plot

    def pie(self,c_1,c_2,c_3):
        factors = pd.concat(
            [
                self.csv[c_1]

            ]
        )
        df = pd.DataFrame({'frame': factors.value_counts()})

        data = px.pie(
            names=df.index,
            values=list(map(lambda x: x[0], df.values.tolist())),
            title=c_1+"Pie chart",
        )

        layout = go.Layout(
            height=600,
            width=1000,
            margin=go.layout.Margin(l=200),
            title=c_1+ "   Pie chart")

        fig = go.Figure(data=data, layout=layout)

        plot = fig.to_html(full_html=False, default_height=500, default_width=600)

        return plot

    def l_regression(self,c_1,c_2,c_3):
        factors = pd.concat(
            [
                self.csv[c_1]

            ]
        )
        df = pd.DataFrame({'counts': factors.value_counts()})
        print(df)

        data= px.scatter(
            df, x=df.index, y=df.counts, opacity=0.65,
            trendline='ols', trendline_color_override='darkblue'
        )

        layout = go.Layout(
            autosize = True,
            height=600,
            width=1000,
            margin=go.layout.Margin(l=200),
            title=c_1 + " liner regression")

        fig = go.Figure(data=data, layout=layout)

        plot = fig.to_html(full_html=False, default_height=500, default_width=700)

        return plot



    def l_regression_2c(self,c_1,c_2,c_3):
        df = self.csv
        data= px.scatter(
            df, x=df[c_2], y=df[c_1], opacity=0.65,
            trendline='ols', trendline_color_override='darkblue'
        )

        layout = go.Layout(
            height=600,
            width=1000,
            margin=go.layout.Margin(l=200),
            title=c_1 + " liner regression")

        fig = go.Figure(data=data, layout=layout)

        plot = fig.to_html(full_html=False, default_height=500, default_width=700)



        return plot

    def bubble_chart(self, c_1, c_2, c_3):
            # print('bubble chart in plot')

            # dfx = pd.DataFrame({'frame':self.csv[[c_2,c_3]].value_counts()})
            # print(dfx)
            # print(dfx.index)
            # print(dfx.frame)

            data = go.Scatter(
                x=self.csv[c_2],
                y=self.csv[c_3],
                mode='markers'

            )

            layout = go.Layout(
                height=600,
                width=500,
                margin=go.layout.Margin(l=200),
                title=c_1 + "Bubble Chart")

            fig = go.Figure(data=data, layout=layout)

            plot = fig.to_html(full_html=False, default_height=500, default_width=700)

            return plot

    def LineChart(self, col, c_1, c_2):
            data = px.line(self.csv, x=self.csv[c_1], y=self.csv[c_2])

            layout = go.Layout(
                height=600,
                width=1000,
                margin=go.layout.Margin(l=200),
                title=c_1 + "Line Chart")

            fig = go.Figure(data=data, layout=layout)

            plot = fig.to_html(full_html=False, default_height=500, default_width=700)

            return plot

    def DotPlot(self, col, c_1, c_2):
            label = self.csv[c_1].unique()

            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=self.csv[c_2].values.tolist() * 2,
                y=label,
                marker=dict(color="crimson", size=12),
                mode="markers",
                name=label[0],
            ))
            fig.add_trace(go.Scatter(
                x=self.csv[c_2].values.tolist() * 3,
                y=label,
                marker=dict(color="gold", size=12),
                mode="markers",
                name=label[1],
            ))

            fig.add_trace(go.Scatter(
                x=self.csv[c_2].values.tolist() * 4,
                y=label,
                marker=dict(color="black", size=12),
                mode="markers",
                name=label[2],
            ))

            plot = fig.to_html(full_html=False, default_height=500, default_width=700)
            return plot
















