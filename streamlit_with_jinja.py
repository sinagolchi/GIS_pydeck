import requests_html
import streamlit as st
import jinja2
import streamlit.components.v1 as components
from PIL import ImageColor
import requests_html
from jinja2 import Environment, FileSystemLoader
st.set_page_config(layout="wide")
st.title("Responsive PyDeck Editing")
with st.sidebar:
    lat = st.number_input(label='Initial lat',value=33.97042155783605)
    long = st.number_input(label='Initial long',value=-118.427226572252)
    zoom = st.number_input(label='Initial zoom',value=14)
    hex = st.color_picker(label="polygon color")
    RGB = list(ImageColor.getcolor(hex, "RGB"))
    title = st.text_input(label='Title',value='Scenario 1')
    cost = st.number_input(label='Total Cost', value=10000)

environment = Environment(loader=FileSystemLoader("Templates/"))
template = environment.get_template("test_map_jinja.html")
description = "<div class=\"deck-json-description-box\" style=\"position: absolute; top: 0px; left: 0px; padding: 1px 12px; overflow: hidden overlay; outline: none; max-height: 94%; box-sizing: border-box; border-bottom-right-radius: 30px; background-color: rgba(0, 255, 255, 0.3); font-family: &quot;Fira Sans&quot;, sans-serif; z-index: 1;\"><div><h2>{title}</h2> <h3>Total Cost: ${cost}</h3></div></div>".format(title=title,cost=cost)

#description = "\"<h2>{title}</h2> </br> <h3>Total Cost: ${cost}</h3>\"".format(title=title,cost=cost)

final_html = template.render(descript=description,ini_lat=lat,ini_long=long,ini_zoom=zoom,color=RGB)


# with open('new_file.html','w') as file:
#     file.write(final_html)

components.html(final_html,height=600)

