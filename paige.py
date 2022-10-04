import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title('---')

cols = ['---']
col_key = st.radio('Which parameter would you like to explore?', options=cols)

df = pd.read_csv('---')

fig = go.Figure(data=go.Choropleth(
    locations=df["Code"], # Spatial coordinates
    z = df[col_key], # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    colorbar_title = "Parameter Strength",
))

fig.update_layout(
    title_text = f'{col_key}',
    geo_scope='usa', # limite map scope to USA
)

fig.show()