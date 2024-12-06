import shiny
from shiny import ui, render, Inputs, Outputs
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Seattle_Buildings_Clusters.csv")
numerical_columns = data.select_dtypes(include=["number"]).columns.tolist()

app_ui = ui.page_fluid(
    ui.h2("Seattle Buildings GHG Emissions Interactive Plot"),
    ui.input_radio_buttons(
        "x_axis",
        "Select X-axis Variable:",
        choices=numerical_columns,
        selected="YearBuilt"
    ),
    ui.output_plot("plot")
)

def server(input: Inputs, output: Outputs, session):
    @output()
    @render.plot
    def plot():
        x_var = input.x_axis()
        if x_var not in numerical_columns:
            return None
        
        plt.figure(figsize=(8, 6))
        plt.scatter(data[x_var], data["GHGEmissionsIntensity"], color="blue", alpha=0.7)
        plt.xlabel(x_var)
        plt.ylabel("GHG Emissions Intensity")
        plt.title(f"GHG Emissions Intensity vs {x_var}")
        plt.grid(True)
        
        return plt.gcf()