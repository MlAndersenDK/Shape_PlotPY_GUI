# Interactive Python shapeplot, to visualize the impact of increased land usage. 
  - A map of the continential USA, divided into states. 

## Overview

This project demonstrates how to create a custom TkInter GUI application for plotting geographical data using GeoPandas and Matplotlib. The application allows users to input a value representing the area in hectares and visualize the corresponding geographical regions on the map. 

## Intented usage:
    The application is intented for free-use visualization of increased land usage in agricultural production. It was originally     developed to display the area impact of increased crop production to satisfy demand for bio-based fuel.  

## Features

- Interactive GUI built with TkInter.
- Plotting functionality using GeoPandas and Matplotlib.
- Supports customization of appearance and plot parameters.
- Ability to reset the plot to its initial state.
- converstion between [m2, km2, ha]

## Requirements

- Python 3.x
- CustomTkinter
- GeoPandas
- Matplotlib

## Installation

1. Clone this repository to your local machine
2. Navicate to directory
3. Install requirements (pip install -r requirements.txt). 
4. Execute the main.py file
5. Interactive with the plot tool in the Custom TKInter window (fullscreen recommended)

## Functionality
#Call plot: 
The slider and entry widget operates with biderectional functionality. Choose either to selected desired area, click: Update plot. 
<img width="1317" alt="Screenshot 2024-02-20 at 11 20 09 AM" src="https://github.com/MlAndersenDK/Shape_PlotPY_GUI/assets/125737851/4b453376-35f2-49a6-acc5-bb50ce049254">

#Reset plot: 
Use the reset botton to reset values and call and empty plot.
<img width="1440" alt="Reset_button" src="https://github.com/MlAndersenDK/Shape_PlotPY_GUI/assets/125737851/4307212d-03e1-4091-9639-760acd70a520">

#Apply the build-in metric conversion:
Use the drop-down menu besides the entry widget, to choose unit [m2,km2,ha], enter number in the widget and HIT ENTER, the engine with convert it to hectares, and update the slider value. To call the new plot; hit Update.

<img width="399" alt="choose_metrics" src="https://github.com/MlAndersenDK/Shape_PlotPY_GUI/assets/125737851/3913bb71-17aa-4aec-938a-afff18815861">

<img width="374" alt="Screenshot 2024-02-20 at 11 52 40 AM" src="https://github.com/MlAndersenDK/Shape_PlotPY_GUI/assets/125737851/56631c74-cc44-4d32-934a-4b94e742a46a">

<img width="1440" alt="conversion_update" src="https://github.com/MlAndersenDK/Shape_PlotPY_GUI/assets/125737851/977f68b3-c3ad-437a-a20a-23a332193547">


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


