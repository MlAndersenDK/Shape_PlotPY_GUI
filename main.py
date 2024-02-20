
import customtkinter as ctk
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from plot import plot_function 

#Import Interface
from gui import GUI

# Import variables
from variables import variables_dict

# Define the shape path
shape_path = 'data/cb_2018_us_state_500k.shp'

Slider_max = variables_dict['Slider_max']

class ctkApp:
        
    def __init__(self):
        ctk.set_appearance_mode("dark")
        self.root = ctk.CTk()
        self.root.geometry("1300x600+200x200")
        self.root.title("Custom TkInter Plot test")
        self.root.update()
        
        self.gui = GUI(self.root, shape_path, Slider_max, self.update_entry_value, self.update_slider_value, self.update_window, self.reset_values)

        self.root.mainloop()
 
    #METHODS     
    def reset_values(self):
        # Reset input, slider, and plot
        self.gui.input.delete(0, 'end')
        self.gui.input.insert(0, '0')
        self.gui.user_input = 0
        self.gui.slider.set(0)
        self.gui.slider_value_label.configure(text=f"Value: {0} hectares")
        #Call method to create empty plot
        #self.update_entry_value()
        self.update_window(0)
   
    
    def update_window(self, value=None):
     #Updates plot by value retrived from get_user_input method 
        if value is not None:
         user_input_hectares = value 
        else:
         user_input_hectares = self.get_user_input()  # Get user input from either entry or slider
         
        fig, ax = plot_function(user_input_hectares, shape_path)
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.33, rely=0.1)
        
        # Update label
        title_variable = "{:,.0f}".format(float(user_input_hectares))
        info_text = f"{title_variable} hectares"  # add number of states covered from covered_states variable
        self.info_label = ctk.CTkLabel(master=self.root, 
                                        text=info_text,
                                        width=340,
                                        height=75,
                                        bg_color="white",
                                        text_color="black")
        self.info_label.place(relx=0.025, rely=0.1)
        self.root.update()
        
    def update_slider_value(self, value):
        # Update entry widget with slider value
        self.gui.input.delete(0, 'end')
        self.gui.input.insert(0, value)
        # Update user_input
        self.user_input = int(value)
        # Update slider value label
        formatted_value = "{:,.0f}".format(float(value))
        self.gui.slider_value_label.configure(text=f"Value: {formatted_value} hectares")  
      
    def update_entry_value(self, event=None):
        try:
            value = float(self.gui.input.get())
            unit = self.gui.unit_combobox.get()
            if unit == "m²":
                value /= 10000  # Convert square meters to hectares
            elif unit == "km²":
                value *= 100  # Convert square kilometers to hectares
            if 0 <= value <= Slider_max:
                self.gui.slider.set(value)
                self.user_input = value
                formatted_value = "{:,.0f}".format(value)
                self.gui.slider_value_label.configure(text=f"Value: {formatted_value} hectares") 
                self.gui.input.delete(0, 'end')
                self.gui.input.insert(0, formatted_value)
            else:
                raise ValueError("Value must be between 0 and {}".format(Slider_max))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
    def get_user_input(self):
        return self.user_input

if __name__ == "__main__":
    CTK_Window = ctkApp()
