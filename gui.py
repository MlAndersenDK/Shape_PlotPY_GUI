import customtkinter as ctk

from variables import variables_dict

Slider_max = variables_dict['Slider_max']

class GUI:
    def __init__(self,root, shape_path, Slider_max, update_entry_value, update_slider_value, update_window, reset_values): 
        self.root = root 
        self.frame = ctk.CTkFrame(master=self.root,
                                  height=self.root.winfo_height()*0.7,
                                  width=self.root.winfo_width()*0.66
                                  )
        self.frame.place(relx=0.33, rely=0.1)
        
        # Initialize user_input variable
        self.user_input = 0
       
       # Combobox - Drop-down menu
        self.unit_combobox = ctk.CTkComboBox(master=self.root, values=["ha","m²", "km²"], height=50, width=variables_dict['drop_down_width'])
        self.unit_combobox.place(relx=0.025, rely=0.5)
        self.unit_combobox.set("ha")
        self.unit_combobox.bind("<<ComboboxSelected>>", update_entry_value)
        
        
        #Self-entry menu
        self.input = ctk.CTkEntry(master=self.root,
                                  placeholder_text="Choose unit, enter value then press enter",
                                  justify='center',
                                  width=variables_dict['entry_width'],
                                  height=50,)
        self.input.place(relx=0.1, rely=0.5)
        self.input.bind('<Return>', update_entry_value)  
        
        
        #SLIDEr
        self.slider_value_label = ctk.CTkLabel(master=self.root, text="Slide to choose area in hectares")
        self.slider_value_label.place(relx=0.025, rely=0.65)

        self.slider = ctk.CTkSlider(master=self.root,
                                    width=340,
                                    height=20,
                                    from_=0,
                                    to=Slider_max,
                                    number_of_steps=250,
                                    command=update_slider_value)
        self.slider.place(relx=0.025, rely=0.7) 
        self.slider.set(0)
        
        #UPDATE button
        self.button = ctk.CTkButton(master=self.root,
                                     text="Update Plot",
                                     width=340,
                                     height=50,
                                     command=update_window)
        self.button.place(relx=0.025, rely=0.25)
        
        #Reset button
        self.reset_button = ctk.CTkButton(master=self.root,
                                          text='Reset',
                                          width=340,
                                          height=50,
                                          command=reset_values)
        self.reset_button.place(relx=0.025, rely=0.35)
