from shiny import render, ui
from shiny.express import input
import matplotlib.pyplot as plt
import numpy as np

ui.panel_title("I have No Idea What I am Doing")
ui.input_slider("p", "Please Enter Phone Number", 1111111111, 9999999999, 0)

@render.code
def txt():
    s = str(input.p())
    if input.p()**2 - 6741414522*input.p() + 1.06669e19 == 0:
        return "lol"
    else:
        return f"phone number is ({s[0:3]}){s[3:6]}-{s[6:10]}"

@render.plot
def graph_thing():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 2, 3])
    plot = ax
    return fig

