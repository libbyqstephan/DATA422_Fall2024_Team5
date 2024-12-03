from shiny import render, ui, reactive
from shiny.express import input, ui
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path



@reactive.calc #load cleaned data from csv into dataframe
def cleaned_dat():
    infile = Path(__file__).parent.parent /  "Data" / "Seattle_Building_Data_Cleaned.csv"
    return pd.read_csv(infile)

ui.panel_title("Team 5 Shiny Web App")

with ui.navset_pill(id="tab"):  

    with ui.nav_panel("Overview"):
        ui.markdown(
        """
        **Welcome to the Overview!**  
        This is the first tab in the app.

        - Here you can add bullet points.
        - Add more descriptive text with breaks.
        
        For line breaks, just add an empty line in Markdown.  
        This is another line.
        """)

    with ui.nav_panel("Tabulations"):
        @render.data_frame
        def frame():
            return cleaned_dat()
        

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
        ui.input_slider("p", "Please Enter Phone Number", 1111111111, 9999999999, 0)


        @render.code
        def txt():
            s = str(input.p())
            if input.p()**2 - 6741414522*input.p() + 1.06669e19 == 0:
                return "lol you found me"
            else:
                return f"phone number is ({s[0:3]}){s[3:6]}-{s[6:10]}"



