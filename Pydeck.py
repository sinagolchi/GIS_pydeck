import pandas as pd
import pydeck as pdk
import json
import numpy as np
import geopandas as gpd
import streamlit as st
from PIL import ImageColor
import streamlit.components.v1 as components

@st.experimental_singleton
def load_data():
    df = gpd.read_file('LA.zip')
    df = df.explode(index_parts=True)
    df = df.to_crs("EPSG:4326")
    return df

df = load_data()


hex = st.color_picker(label="polygon color")
with st.sidebar:
    RGB =list(ImageColor.getcolor(hex, "RGB"))


# def build_deck():
#     building = pdk.Layer(type='PolygonLayer',data=df, get_polygon="geometry.coordinates",
#         stroked=False,filled=True,extruded=True,get_elevation='HEIGHT',get_fill_color=str(RGB),auto_highlight=True,
#         pickable=True)
#
#     tooltip = {"html": "<b>Building height:</b> {HEIGHT} </br> <b>Building Elevation:</b> {ELEV}"}
#
#     view_point = pdk.ViewState(latitude=33.9986, longitude=-118.4175, zoom=11, max_zoom=20, pitch=45, bearing=0)
#
#     r = pdk.Deck(layers=[building],initial_view_state=view_point,map_style=pdk.map_styles.LIGHT,tooltip=tooltip)
#     return r

# components.html(build_deck().to_html(as_string=True),height=600)

def map(data, lat, lon, zoom,color):
    st.write(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state={
                "latitude": lat,
                "longitude": lon,
                "zoom": zoom,
                "pitch": 50,
            },
            layers=[
                pdk.Layer(
                    "PolygonLayer",
                    data=data,
                    get_polygon="geometry.coordinates",
                    get_elevation='HEIGHT',
                    get_fill_color=str(color),
                    pickable=True,
                    extruded=True,
                ),
            ],
        )
    )

map(data=df,lat=33.9986,lon=-118.4175,zoom=11,color=RGB)