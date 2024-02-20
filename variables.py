from capacity_engine import max_capacity
import os

shape_path = os.path.abspath('data/cb_2018_us_state_500k.shp')

variables_dict = {
 'widget_width':340,
 'entry_width':250,
 'drop_down_width':90,
 'Slider_max': max_capacity(shape_path) 
}
