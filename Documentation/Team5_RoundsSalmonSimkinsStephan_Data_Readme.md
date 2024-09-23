This dataset was sourced from the city of seattle website which can be found [here](https://data.seattle.gov/Permitting/2022-Building-Energy-Benchmarking/5sxi-iyiy/about_data). The dataset is maintained and published on a quarterly basis by the City of Seattle Office of Sustainability and Environment.

Please see the data dictionary for the schema and field descriptions. The integrity of the data is fairly good, some columns contain missing values because of missing building features (i.e. building has steam).

The dataset contains 3653 total rows, and each row represents an individual building or property that contains multiple buildings. It also has 42 columns representing different attributes, measurements, or features of each property/building. In total it has 153,426 individual data points.

The dataset can be joined across the OSEBuildingID column or the composite key of Address + City + State + Zipcode. The dataset will need some column types to be changed before using. Null values also need to be handled.

The dataset is saved in a comma separated value (.csv) format and only takes up 1.12 megabytes (MB) of space, this is small enough to store in the github repository.