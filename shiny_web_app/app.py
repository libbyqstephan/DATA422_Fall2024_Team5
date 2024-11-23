from shiny import render, ui
from shiny.express import input, ui
import matplotlib.pyplot as plt
import numpy as np

with ui.navset_pill(id="tab"):  
    with ui.nav_panel("Overview"):
        "Panel A content"

    with ui.nav_panel("Tabulations"):
        "Panel B content"

    with ui.nav_panel("Visuals & Charts"):
        "Panel C content"
        @render.plot
        def graph_thing():
            fig, ax = plt.subplots()
            ax.plot([1, 2, 3], [1, 2, 3])
            plot = ax
            return fig


    with ui.nav_panel("Models"):
        "Page D content"
        
    with ui.nav_panel("test"):
        ui.panel_title("I have No Idea What I am Doing")
        ui.input_slider("p", "Please Enter Phone Number", 1111111111, 9999999999, 0)


        @render.code
        def txt():
            s = str(input.p())
            if input.p()**2 - 6741414522*input.p() + 1.06669e19 == 0:
                return "lol you found me"
            else:
                return f"phone number is ({s[0:3]}){s[3:6]}-{s[6:10]}"



