from shiny import render, ui, reactive
from shiny.express import input, ui
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.tree import DecisionTreeClassifier, plot_tree

dtc_data = pd.read_csv(Path(__file__).parent.parent / "Data" / "Seattle_Building_Clusters.csv")
dtc_data = dtc_data.drop(columns=['OSEBuildingID','BuildingName', 'BuildingType', 'Address', 'Neighborhood', 'EPAPropertyType', 'ComplianceStatus', 'ComplianceIssue', 'GHGEmissionsIntensity'])
dtc_data = dtc_data.dropna()
X = dtc_data[['Electricity(kBtu)', 'SteamUse(kBtu)', 'NaturalGas(kBtu)', 'PropertyGFATotal', 'SourceEUI(kBtu/sf)']]
y = dtc_data[['GHGIntensityCluster']]

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
        ui.markdown(
            """This is the Tabulations tab of the app.
            Here you can see the data formatted as a table.
            
        """)
        @render.data_frame
        def frame():
            return dat()

        

    with ui.nav_panel("Visuals & Charts",):
        ui.markdown(
                """
                ### Interactive Map of Building Locations
                """
        )

        # slider histogram of YearBuilt
        ui.input_slider("n_bins", "Number of bins", 1, 100, 20)

        @render.plot(alt="A histogram of year built")
        def plot_histogram():
            # Load the reactive dataset
            df = dat()

            # Choose a column for the histogram (adjust as needed)
            column_data = df["YearBuilt"]

            # Plot the histogram
            fig, ax = plt.subplots()
            ax.hist(column_data, bins=input.n_bins(), density=True)
            ax.set_title("Property Year Built")
            ax.set_xlabel("Year Built")
            ax.set_ylabel("Count")

            return fig


    with ui.nav_panel("Models"):
        ui.markdown(
            """
            ### Interactive Decision Tree Classifier
            Use the sliders to input the values for the features and see how the path that the decision tree classifier uses to classify the input changes.
            """
        )
        ui.input_slider("Electricity", "Electricity (kBtu)", min(X['Electricity(kBtu)']), max(X['Electricity(kBtu)']), step=1, value=min(X['Electricity(kBtu)'])),
        ui.input_slider("SteamUse", "Steam Use (kBtu)", min(X['SteamUse(kBtu)']), max(X['SteamUse(kBtu)']), step=1, value=min(X['SteamUse(kBtu)'])),
        ui.input_slider("NaturalGas", "Natural Gas (kBtu)", min(X['NaturalGas(kBtu)']), max(X['NaturalGas(kBtu)']), step=1, value=min(X['NaturalGas(kBtu)'])),
        ui.input_slider("PropertyGFATotal", "Property GFA Total", min(X['PropertyGFATotal']), max(X['PropertyGFATotal']), step=1, value=min(X['PropertyGFATotal'])),
        ui.input_slider("SourceEUI", "Source EUI (kBtu/sf)", min(X['SourceEUI(kBtu/sf)']), max(X['SourceEUI(kBtu/sf)']), step=1, value=min(X['SourceEUI(kBtu/sf)'])),
        
        @render.plot #Plot the decision tree and mark the path it takes based on the input sliders
        def decision_tree_plot():
            clf = train_classifier()
            fig, ax = plt.subplots(figsize=(40, 40), dpi=150)
            plot_tree(clf, feature_names=['Electricity(kBtu)', 'SteamUse(kBtu)', 'NaturalGas(kBtu)', 'PropertyGFATotal', 'SourceEUI(kBtu/sf)'], filled=False, ax=ax)

         #Create a sample with the correct feature names
            sample = pd.DataFrame({
                'Electricity(kBtu)': [input['Electricity']()],
                'SteamUse(kBtu)': [input['SteamUse']()],
                'NaturalGas(kBtu)': [input['NaturalGas']()],
                'PropertyGFATotal': [input['PropertyGFATotal']()],
                'SourceEUI(kBtu/sf)': [input['SourceEUI']()]
            })

            #Get the decision path for the sample
            path = clf.decision_path(sample).toarray().astype(bool)[0]
            node_indicator = clf.decision_path(sample)
            leaf_id = clf.apply(sample)

            #Highlight the nodes in the path
            for node_id in np.where(path)[0]:
                if isinstance(ax.get_children()[node_id], plt.Text):
                    ax.get_children()[node_id].set_bbox(dict(facecolor='yellow', alpha=0.5))

            #Add an arrow to the bottom-most node
            bottom_node = np.where(path)[0][-1]
            if isinstance(ax.get_children()[bottom_node], plt.Text):
                bbox = ax.get_children()[bottom_node].get_window_extent()
                center = bbox.transformed(ax.transData.inverted()).get_points().mean(axis=0)
                ax.annotate('Decision Node', xy=center,
                            xytext=(center[0], center[1] - 0.1),
                            arrowprops=dict(facecolor='Red', shrink=0.05))

            return fig
        
        
    with ui.nav_panel("test"):
        ui.input_slider("p", "Please Enter Phone Number", 1111111111, 9999999999, 0) #add slider for phone number, value goes to input.p()


        @render.code
        def txt(): #code to display the phone number formatted
            s = str(input.p())
            if input.p()**2 - 6741414522*input.p() + 1.06669e19 == 0:
                return "lol you found me"
            else:
                return f"phone number is ({s[0:3]}){s[3:6]}-{s[6:10]}"
            
            
@reactive.calc #reactive function to train the decision tree classifier model
def train_classifier():
    clf = DecisionTreeClassifier(ccp_alpha = 0.001, 
                                 max_depth = 10, 
                                 max_leaf_nodes = 90, 
                                 min_samples_leaf = 1, 
                                 min_samples_split = 15,
                                 random_state = 42)
    clf.fit(X, y)
    return clf

@reactive.calc #reactive function to load the cleaned data
def dat():
    cleaned_data_file = Path(__file__).parent.parent / "Data" / "Seattle_Building_Data_Cleaned.csv"
    data = pd.read_csv(cleaned_data_file)
    data = data.drop(columns=["DataYear", "ZipCode", "OSEBuildingID"]) #removing these columns because it reduces clutter
    return data



