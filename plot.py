import geopandas as gpd
import matplotlib.pyplot as plt

def plot_function(user_input_hectares, shape_path):
    shape = gpd.read_file(shape_path)
    shape = shape.to_crs(epsg=3857)

    states_to_drop = ['Alaska','Hawaii','Puerto Rico', 'American Samoa', 'United States Virgin Islands', 'Guam', 'Commonwealth of the Northern Mariana Islands']
    shape = shape[~shape['NAME'].isin(states_to_drop)]
    shape['State_Area_hectares'] = shape.geometry.area / 10**4
   
    #user_input_sqm = user_input_hectares * 10000
    title_variable = "{:,.0f}".format(float(user_input_hectares))

    total_area_covered = 0
    covered_states = []

    for index, row in shape.iterrows():
        state_area = row['State_Area_hectares']
        if total_area_covered + state_area <= user_input_hectares:
            total_area_covered += state_area
            covered_states.append(row['NAME'])
        else:
            break

    covered_states_df = shape[shape['NAME'].isin(covered_states)]

    fig, ax = plt.subplots(figsize=(8, 5))
    shape.boundary.plot(ax=ax, edgecolor='black', linewidth=0.2)
    covered_states_df.plot(ax=ax, color='green')
    
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    for edge in ['right','bottom','top','left']:
        ax.spines[edge].set_visible(False)
   
    title = f"{title_variable} hectares cover {len(covered_states)} states"
    ax.set_title(title)

    return fig, ax


