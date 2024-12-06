#import shiny
from shiny import ui, render, Outputs
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("Seattle_Buildings_Clusters.csv")


choices = data["GHGIntensityCluster"].unique().astype(str)
selected = data["GHGIntensityCluster"].unique().astype(str)

app_ui = ui.page_fluid(
    ui.h2("GHG Emissions Intensity vs Year Built"),
    ui.input_checkbox_group(
        "clusters",
        "Select GHG Intensity Clusters to Display:",
        choices=choices.tolist(),
        selected=selected.tolist()
    ),
    ui.output_plot("plot") 
)

def server(input, output, session):
    @output()
    @render.plot
    def plot():
        filtered_data = data[data["GHGIntensityCluster"].isin(input.clusters())]
        
        plt.figure(figsize=(8, 6))
        for cluster in filtered_data["GHGIntensityCluster"].unique():
            cluster_data = filtered_data[filtered_data["GHGIntensityCluster"] == cluster]
            plt.scatter(cluster_data["YearBuilt"], cluster_data["Emissions"], label=f"Cluster {cluster}")
        
        plt.xlabel("Year Built")
        plt.ylabel("Emissions")
        plt.title("GHG Emissions Intensity vs Year Built")
        plt.legend()
        
        return plt.gcf()

app = shiny.App(app_ui, server)