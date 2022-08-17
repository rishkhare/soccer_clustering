import streamlit as st
import pandas as pd
import numpy as np
import bokeh
from bokeh.models import (
    ColumnDataSource,
    HoverTool,
    LinearColorMapper,
    CustomJS,
    Slider,
    TapTool,
    TextInput,
)
from bokeh.palettes import Category20
from bokeh.transform import linear_cmap, transform
from bokeh.io import output_file, show, output_notebook
from bokeh.plotting import figure
from bokeh.models import RadioButtonGroup, TextInput, Div, Paragraph
from bokeh.layouts import column, widgetbox, row, layout
from bokeh.layouts import column

st.title("Soccer players grouped according to their traits")

# import data
v2_data = pd.read_csv("data/final_data.csv")
X_embedded = np.loadtxt("data/X.dat")
y_labels = np.loadtxt("data/y_labels.dat")


# data sources
source = ColumnDataSource(
    data=dict(
        x=X_embedded[:, 0],
        y=X_embedded[:, 1],
        x_backup=X_embedded[:, 0],
        y_backup=X_embedded[:, 1],
        desc=y_labels,
        player_name=v2_data["Player Name"],
        att_def=v2_data["Playing_Nature"],
        vert_pos=v2_data["Vertical Position"],
        horizontal_pos=v2_data["Horizontal Position"],
        rating=v2_data["Rating"],
        labels=["C-" + str(int(x)) for x in y_labels],
    )
)

# hover over information
hover = HoverTool(
    tooltips=[
        ("Player Name", "@player_name{safe}"),
        ("Player Nature", "@att_def{safe}"),
        ("Vertical Position", "@vert_pos{safe}"),
        ("Horizontal Position", "@horizontal_pos{safe}"),
        ("Rating", "@rating"),
        ("Cluster", "@labels"),
    ],
    point_policy="follow_mouse",
)

# map colors
mapper = linear_cmap(
    field_name="desc", palette=Category20[6], low=min(y_labels), high=max(y_labels)
)

# prepare the figure
plot = figure(
    plot_width=1200,
    plot_height=850,
    tools=[hover, "pan", "wheel_zoom", "box_zoom", "reset", "save", "tap"],
    toolbar_location="above",
)

# plot settings
plot.scatter(
    "x",
    "y",
    size=5,
    source=source,
    fill_color=mapper,
    line_alpha=0.3,
    line_color="black",
    legend="labels",
)
plot.legend.background_fill_alpha = 0.6

# deploy on streamlit
st.bokeh_chart(plot, use_container_width=True)
