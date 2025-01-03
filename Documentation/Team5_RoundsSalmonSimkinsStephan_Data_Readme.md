Data Summary
Team 5
Data 422
9/27/24

The data we are analyzing is comprised of a dataset collected by the City of Seattle through their Energy Benchmarking Program. This initiative aims to track and report energy performance throughout the city to increase transparency about the price of heat and energy for potential homeowners before they buy the home and realize maintenance expenses are high. As an additional benefit of this increased level of information, lawmakers are expecting energy efficiency to become a greater focus in the creation of buildings in the future since efficient homes are also cheaper. This yearly collection of data provides a rigorous set of information for our purposes and is directly in line with our goal of predicting the overall energy efficiency of a building, as well as identifying which type of building is most efficient. 

The factors in this dataset are somewhat unique in their level of detail. The dataset includes information about the building itself, such as the type of fuel they use for heat and electricity, their overall greenhouse gas emissions, and primary uses for the building, but also the level of compliance with the ordinance in the past year. Several different kinds of buildings are represented, from schools, office buildings, hotels, and self-storage units, which builds even more variety and context for the analysis to come. We anticipate that this increased level of variety will lead our models to be even more accurate on any building in Seattle because so many are represented. 

The dataset contains information from the year 2022 with 3654 rows, each representing a building, and 42 columns. This provides an ample sample size. 

We do not plan on joining our datasets since the information from year 2022 is sufficient. If we were to join them however, we would do it on the unique building identifier for each building in Seattle that was considered in this dataset. We plan on removing columns that are primarily empty or not directly necessary to our overall research question. For example, the Third Largest Property Use Type column will be removed since it is primarily empty due to the scarcity of buildings that are large enough to have three major property uses. Once these excess columns are removed, we will identify rows with N/A or NaN values and remove the ones that do not contain enough information to be considered in our investigation. After these initial steps are completed, additional cleaning specific to certain analysis may occur. 

This data is currently being read from the original .csv files and stored in Python dataframes. This method will continue to be the primary means of storage due to the manageable size of the dataset and the ease of use and access once analysis begins. 
