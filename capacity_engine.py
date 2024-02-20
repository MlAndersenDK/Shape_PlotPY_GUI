import numpy as np
import geopandas as gpd

def max_capacity(shape_path):
    shape = gpd.read_file(shape_path)
    shape = shape.to_crs(epsg=3857)
    states_to_drop = ['Alaska','Hawaii','Puerto Rico', 'American Samoa', 'United States Virgin Islands', 'Guam', 'Commonwealth of the Northern Mariana Islands']
    shape = shape[~shape['NAME'].isin(states_to_drop)]
    shape['State_Area_hectares'] = shape.geometry.area / 10**4
    total_size = sum(shape['State_Area_hectares'])
    return total_size
   
