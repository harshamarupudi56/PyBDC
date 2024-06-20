#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:21:41 2023

@author: DIDSR
"""

#%% import necessary modules

from tkinter import filedialog, Menu, IntVar, W
import customtkinter 
import numpy as np 
from matplotlib.pyplot import style as plt_style, ioff as plt_ioff, figure as plt_figure, rcParams as params
plt_ioff() # suppress pyplot popups
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sys 
from dose_equations import Sarno_mono_dgn, Sarno_poly_dgn, sarno_dgnct, Hernandez_hetero_mono_dgn, exposure_per_fluence, Sechopoulos_poly_dgn 


#%% important functions

# quit me function
def quit_me(): 
    root.quit()
    root.destroy()

# calculate pDgN
def calculate_pDgNct(*values):
    keV = values[2]; I = values[3];
    psiE = np.array(list(map(exposure_per_fluence,keV)))
    
    if values[0] == 'Sarno Koning':
        variables = values[1]
        DgNctE = np.array(list(map(sarno_dgnct,variables[:,0],variables[:,1],variables[:,2],variables[:,3],
                                   variables[:,4],variables[:,5],variables[:,6],variables[:,7],keV)));    
        pDgN = np.sum(I*psiE*DgNctE)/np.sum(I*psiE);
    
    elif values[0] == 'Hernandez':
        DgN_list = np.array(values[1])
        pDgN = np.sum(I*psiE*DgN_list)/(np.sum(I*psiE))
    
    return pDgN

# read method outputs
with open('method_specific_inputs.txt','r') as file:
     data = file.readlines() # all the outputs
     

#%%% Main code

class Main_Window():
    
    #%% build the gui frames
    def __init__(self, master):     
        
        self.master = master
        # create the menubar
        menubar = Menu(master)
        root.config(menu=menubar)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Quick Start Guide", command=self.help_command)
        helpmenu.add_command(label="About", command=self.about)
        menubar.add_cascade(label="Help", menu=helpmenu)
        menubar.add_command(label="Exit", command=lambda: quit_me())

        # create the different frames
        self.methods_frame = customtkinter.CTkFrame(master=master)
        self.methods_frame.grid(row=0,column=0, ipady=36)
        self.inputs_frame = customtkinter.CTkFrame(master=master)
        self.inputs_frame.grid(row=0,column=1, padx=10, pady=5, ipadx=6)
        self.kerma_spec_frame = customtkinter.CTkFrame(master=master)
        self.kerma_spec_frame.grid(row=0,column=2, pady=5, ipady=24,ipadx=4)
        self.output_frame = customtkinter.CTkFrame(master=master)
        self.output_frame.grid(row=1,column=0,ipady=12)
        self.graph_frame = customtkinter.CTkFrame(master=master)
        self.graph_frame.grid(row=1,column=1, columnspan=2,padx=4,ipady=14)
        # create figure
        self.keV = []; self.I = []
        self.plot_spectra()
        
        #%% add the different methods
        self.method_label = customtkinter.CTkLabel(master=self.methods_frame, text="Choose any of the following BCT methods:")
        self.method_chosen = IntVar(root)
        self.method_chosen.set(2)
        self.current_method = 1
        self.Sarno_radiobutton = customtkinter.CTkRadioButton(master=self.methods_frame, text="Sarno 49 kVp W Spectra",
                                                     command=lambda: self.change_inputs(), variable= self.method_chosen,
                                                     value=1, radiobutton_width = 14, radiobutton_height=14)

        self.Sarno_incident_radiobutton = customtkinter.CTkRadioButton(master=self.methods_frame, text="Sarno Any Spectrum",
                                                     command=lambda: self.change_inputs(), variable= self.method_chosen, 
                                                     value=2, radiobutton_width = 14, radiobutton_height=14)

        self.Hernandez_radiobutton = customtkinter.CTkRadioButton(master=self.methods_frame, text="Hernandez Any Spectrum",
                                                     command=lambda:self.change_inputs(), variable= self.method_chosen, 
                                                     value=3, radiobutton_width = 14, radiobutton_height=14)
        
        self.Sechopoulos_radiobutton = customtkinter.CTkRadioButton(master=self.methods_frame, text="Sechopoulos 49 kVp W Spectra",
                                                     command=lambda:self.change_inputs(), variable= self.method_chosen, 
                                                     value=4, radiobutton_width = 14, radiobutton_height=14)

        self.method_label.pack(padx=20,pady=5, anchor=W)
        self.Sarno_incident_radiobutton.pack(padx=20, pady=5, anchor=W)
        self.Hernandez_radiobutton.pack(padx=20, pady=5, anchor=W)
        self.Sarno_radiobutton.pack(padx=20, pady=5, anchor=W)
        self.Sechopoulos_radiobutton.pack(padx=20, pady=5, anchor=W)
        
        #%% fill in the main input box
        self.Breast_diameter_label = customtkinter.CTkLabel(master=self.inputs_frame, text = 'Breast Diameter (cm):')
        self.Breast_diameter_combo = customtkinter.CTkComboBox(master=self.inputs_frame, 
                                                              values=['8','10','12','14','19','18'], 
                                                              width=120, state='readonly')
        self.Breast_diameter_combo.set('8')
        
        self.Breast_height_label = customtkinter.CTkLabel(master=self.inputs_frame, text='Breast Height:')
        self.Breast_height_combo = customtkinter.CTkComboBox(master=self.inputs_frame, 
                                                            values=['1 x radius', '1.5 x radius', '2 x radius'],
                                                            width=120, state='readonly')
        self.Breast_height_combo.set('1 x radius')
        self.Breast_glandularity_label = customtkinter.CTkLabel(master=self.inputs_frame, text = 'Breast Glandularity:')
        self.Breast_glandularity_combo = customtkinter.CTkComboBox(master=self.inputs_frame,
                                                                  values=['0.1%', '14.3%', '25%', '50%', '100%'],
                                                                  width=120, state='readonly')
        self.Breast_glandularity_combo.set('0.1%')
        
        self.HVL_label = customtkinter.CTkLabel(master=self.inputs_frame, text='HVL (mm Al):')
        self.HVL_combo = customtkinter.CTkComboBox(master=self.inputs_frame, 
                                              values=['1.25','1.30','1.35','1.40','1.45','1.50'], 
                                              width=120, state='readonly')
        self.HVL_combo.set('1.25')
         
        self.VGF_label = customtkinter.CTkLabel(master=self.inputs_frame,text='Heterogeneous Categories:')
        self.VGF_combo =customtkinter.CTkComboBox(master=self.inputs_frame,                      
                                             values=['V1 = 19.9%','V3 = 9.5%','V5 = 3.8%'], 
                                             width=120, state='readonly') # V1 = 19.9%, V3 = 9.5%, V5 = 3.8%
        self.VGF_combo.set('V1 = 19.9%')
        self.input_spectra_button = customtkinter.CTkButton(master=self.inputs_frame,
                                                            fg_color=("black", "lightgray"),
                                                       width=100,
                                                       border_width=0,
                                                       corner_radius=2,
                                                       text="Upload Incident Spectrum File",
                                                       font = ('Roman',14),
                                                       command=lambda:self.browse_files())
        self.Breast_diameter_label.grid(row=0,column=0,pady=5,padx=4,sticky=W)
        self.Breast_diameter_combo.grid(row=0,column=1,pady=5, padx=10, sticky=W)
        self.Breast_height_label.grid(row=1,column=0, pady=5,padx=4,sticky=W)
        self.Breast_height_combo.grid(row=1, column=1, pady=5)
        self.Breast_glandularity_label.grid(row=2,column=0,pady=5,padx=4,sticky=W)
        self.Breast_glandularity_combo.grid(row=2,column=1,pady=5)
        self.HVL_label.grid(row=3, column=0,pady=5,padx=4,sticky=W)
        self.HVL_combo.grid(row=3, column=1, pady=5)
        self.HVL_combo.configure(state='disabled')
        self.VGF_label.grid(row=4, column=0,pady=5,padx=4,sticky=W)
        self.VGF_combo.grid(row=4, column=1, pady=5,padx=12, sticky=W)
        self.VGF_combo.configure(state='disabled')
        self.input_spectra_button.grid(row=5,column=0, pady=5, columnspan=2)
        
        #%% create text box and buttons for output frame
        self.output_textbox = customtkinter.CTkTextbox(self.output_frame, width=285, height=305)
        self.output_textbox.tag_config('green', foreground='green')
        self.output_textbox.configure(state='normal')
        self.output_textbox.insert("end", f'{"".join(data[0:5])}', 'green')
        self.output_textbox.configure(state='disabled')
        self.clear_button = customtkinter.CTkButton(master=self.output_frame,
                                                       width=120,
                                                       border_width=0,
                                                       corner_radius=8,
                                                       text="Clear Text",
                                                       font = ('Roman',14),
                                                       command=lambda: self.clear_text())
        self.calculate_button = customtkinter.CTkButton(master=self.output_frame,
                                                       width=120,
                                                       border_width=0,
                                                       corner_radius=8,
                                                       text="Calculate Dose",
                                                       font = ('Roman',14),
                                                       command=lambda: self.calculate_dose())
        
        self.clear_button.grid(row=1,column=0,pady=5,padx=4)
        self.output_textbox.grid(row=0,column=0, columnspan=3)
        self.output_textbox.configure(state='disabled') # insert at line 0 character 0
        self.calculate_button.grid(row=1,column=1, pady=5,padx=4)
        
        #%% create air kerma inputs
        
        self.mAs_label = customtkinter.CTkLabel(master=self.kerma_spec_frame, text='mAs per Projection:')
        self.mAs_entry = customtkinter.CTkEntry(master=self.kerma_spec_frame, width=80)
        self.mAs_units_combo = customtkinter.CTkComboBox(master=self.kerma_spec_frame, 
                                                  values=['mAs'], 
                                                  width=80, state='readonly')
        
        self.air_kerma_label = customtkinter.CTkLabel(master= self.kerma_spec_frame, text = 'Air kerma per Projection:')
        self.air_kerma_entry = customtkinter.CTkEntry(master= self.kerma_spec_frame, width=80)
        self.input_label = customtkinter.CTkLabel(master= self.kerma_spec_frame, text="Air kerma Units:")
        self.air_kerma_units_combo = customtkinter.CTkComboBox(master= self.kerma_spec_frame, 
                                                          values=['mrad','mGy','R','mR'], 
                                                          width=80, state='readonly')
        self.air_kerma_units_combo.set('R')
        self.air_kerma_output_label = customtkinter.CTkLabel(master= self.kerma_spec_frame, text='MGD Units:',
                                                             anchor=W)
        self.output_units = customtkinter.CTkComboBox(master= self.kerma_spec_frame, 
                                                 values=['mrad','mGy'], width=80,
                                                 state='readonly')
        self.output_units.set('mrad')
        
        self.number_projections_label = customtkinter.CTkLabel(master= self.kerma_spec_frame, text = 'Number of Projections: ')
        self.number_projections_entry = customtkinter.CTkEntry(master= self.kerma_spec_frame, width=80)
        
        
        self.graph_spectra = customtkinter.CTkButton(master=self.kerma_spec_frame,
                                                       width=220,
                                                       border_width=1,
                                                       corner_radius=10,
                                                       text="Graph Spectrum",
                                                       font = ('Roman',14),
                                                       command=self.plot_spectra)
        
        self.air_kerma_label.grid(row=1, column=0, pady=5, padx=4, sticky=W)
        self.air_kerma_entry.grid(row=1, column=1, pady=5, padx=12, sticky=W)
        self.number_projections_label.grid(row=2, column=0, pady=5, padx=4, sticky=W)
        self.number_projections_entry.grid(row=2, column=1, pady=5, padx=12, sticky=W)
        self.mAs_label.grid(row=5,column =0, pady=5, padx=4, sticky=W) 
        self.mAs_entry.grid(row=5, column =1, pady =5, padx=12, sticky=W)
        self.input_label.grid(row=3, column=0, pady=5, padx=4, sticky=W)
        self.air_kerma_units_combo.grid(row=3, column=1, pady=5, padx=12, sticky=W)
        self.air_kerma_output_label.grid(row=4, column=0, pady=5, padx=4, sticky=W)
        self.output_units.grid(row=4, column=1, pady=5, padx=12, sticky=W)
        self.graph_spectra.grid(row=6,column=0, pady=5, columnspan=2)
        self.graph_spectra.configure(state='disabled')
        
#%% important functions
    # add about command which returns paper citations
    def about(self):
        pop_up = customtkinter.CTkToplevel()
        textbox = customtkinter.CTkTextbox(master=pop_up, width=750, height= 500)
        textbox.pack(fill ='both')
        
        with open('Paper Citations.txt','r') as file:
            text = ""
            data = file.readlines()
            data = "".join(data)
            data = data.replace("â€“",'-')
            text = text + data
            
        textbox.insert('end', f'{text}')
        textbox.configure(state='disabled')
        
    # add help command
    def help_command(self):
       pop_up = customtkinter.CTkToplevel()
       textbox = customtkinter.CTkTextbox(master=pop_up, width=800, height= 500)
       textbox.pack(fill ='both')
       
       with open('CT_Dose_Calculate_Quick_Guide.txt', 'r') as file:
           data = file.read()
           
       textbox.insert("end", f'{data}')
       textbox.configure(state='disabled')
        
    # change the method specific inputs based on selection
    def change_inputs(self):
        current_method = self.method_chosen.get()
        
        if current_method == 1: # Sarno 49 kVp W Spectra
            # enable and disable buttons
            self.VGF_combo.configure(state='disabled')
            self.input_spectra_button.configure(state='disabled')
            self.Breast_diameter_combo.configure(state='normal')
            self.Breast_height_combo.configure(state='normal')
            self.Breast_glandularity_combo.configure(state='normal')
            self.HVL_combo.configure(state='normal')
            self.graph_spectra.configure(state='disabled')
            self.Breast_glandularity_combo.configure(values=['0.1%', '14.3%', '25%', '50%', '75%', '100%'])
            self.Breast_glandularity_combo.set('0.1%')
            self.Breast_diameter_combo.configure(values=['8','10','12','14','19','18'])
            self.Breast_diameter_combo.set('8')
            self.Breast_height_combo.configure(values=['1 x radius', '1.5 x radius', '2 x radius'])
            self.Breast_height_combo.set('1 x radius')
            self.output_textbox.configure(state='normal') # outputs text
            self.output_textbox.insert("end", f'{"".join(data[5:12])}', 'green')
            self.output_textbox.configure(state='disabled')
            self.keV = []; self.I = []; self.plot_spectra()
            
        elif current_method == 2: # Sarno any spectrum
            self.VGF_combo.configure(state='disabled')
            self.input_spectra_button.configure(state='normal')
            self.Breast_diameter_combo.configure(state='normal')
            self.Breast_height_combo.configure(state='normal')
            self.Breast_glandularity_combo.configure(state='normal')
            self.HVL_combo.configure(state='disabled')
            self.graph_spectra.configure(state='disabled')
            self.Breast_glandularity_combo.configure(values=['0.1%', '14.3%', '25%', '50%', '75%', '100%'])
            self.Breast_glandularity_combo.set('0.1%')
            self.Breast_diameter_combo.configure(values=['8','10','12','14','19','18'])
            self.Breast_diameter_combo.set('8')
            self.Breast_height_combo.configure(values=['1 x radius', '1.5 x radius', '2 x radius'])
            self.Breast_height_combo.set('1 x radius')
            self.output_textbox.configure(state='normal')
            self.output_textbox.insert("end", f'{"".join(data[12:19])}', 'green')
            self.output_textbox.configure(state='disabled')
            self.keV = []; self.I = []; self.plot_spectra()
            
        elif current_method == 3: # Hernandez any spectrum
            self.VGF_combo.configure(state='normal')
            self.input_spectra_button.configure(state='normal')
            self.Breast_diameter_combo.configure(state='disabled')
            self.Breast_height_combo.configure(state='disabled')
            self.Breast_glandularity_combo.configure(state='disabled')
            self.HVL_combo.configure(state='disabled')
            self.graph_spectra.configure(state='disabled')
            self.output_textbox.configure(state='normal')
            self.output_textbox.insert("end", f'{"".join(data[12:19])}', 'green')
            self.output_textbox.configure(state='disabled')
            self.keV = []; self.I = []; self.plot_spectra()
            self.output_textbox.configure(state='normal')
            self.output_textbox.insert("end", f'{"".join(data[19:29])}', 'green')
            self.output_textbox.configure(state='disabled')
        
        else:  # Sechopoulus method
            self.VGF_combo.configure(state='disabled')
            self.input_spectra_button.configure(state='disabled')
            self.Breast_diameter_combo.configure(state='normal')
            self.Breast_height_combo.configure(state='normal')
            self.Breast_glandularity_combo.configure(state='normal')
            self.HVL_combo.configure(state='disabled')
            self.graph_spectra.configure(state='disabled')
            self.output_textbox.configure(state='normal')
            self.output_textbox.insert("end", f'{"".join(data[30:35])}', 'green')
            self.output_textbox.configure(state='disabled')
            self.Breast_glandularity_combo.configure(values=['1%', '14.3%', '25%', '50%', '75%', '100%'])
            self.Breast_glandularity_combo.set('1%')
            self.Breast_diameter_combo.configure(values=['10','12','14','19','18'])
            self.Breast_diameter_combo.set('10')
            self.Breast_height_combo.configure(values=['0.5 x diameter', '0.75 x diameter', '1 x diameter'])
            self.Breast_height_combo.set('0.5 x diameter')
            self.keV = []; self.I = []; self.plot_spectra()
     
    # browse for incident spectrum
    def browse_files(self):
        # read and output textfile
        self.input_txt_file = filedialog.askopenfilename(initialdir='/', title='Select a File', filetypes= [('all files','*.*')])
        self.display_txt_file = self.input_txt_file.split('/')[-1]
        self.output_textbox.configure(state='normal')
        self.output_textbox.insert("end", f'\nInputted incident spectrum: \n{self.display_txt_file}', '\n')
        self.output_textbox.configure(state='disabled')
        
        try:
            # get keV and I
            self.keV, self.I = self.read_input_spectra()
            self.minimum = min(self.keV); self.maximum = max(self.keV)
            method = self.method_chosen.get()
            
            if method == 3:
                if self.minimum<9 or self.maximum>70:
                    raise(ValueError)
            elif method == 2:
                if self.minimum<8 or self.maximum>80:
                    raise(ValueError)
            
            self.graph_spectra.configure(state='normal')
        
        # account for possible errors
        except UnicodeDecodeError:
            pop_up = customtkinter.CTkToplevel()
            customtkinter.CTkLabel(pop_up, text='Please enter a valid text file', font=('Roman', 12)).pack()
                
        except ValueError:
            pop_up = customtkinter.CTkToplevel()
            customtkinter.CTkLabel(pop_up, text='For Hernadez Any spectrum, please enter spectrum ranging from 9 to 70 keV', font=('Roman', 12)).pack()
            customtkinter.CTkLabel(pop_up, text='For Sarno Any Spectrum, please enter spectrum ranging from 8 to 80 keV', font=('Roman', 12)).pack()
    
    # read input spectra
    def read_input_spectra(self):
        with open(self.input_txt_file, 'r') as file:
            keV = []; I = []
            data = file.readlines()
            for line in data:
                line  = line.split()
                keV.append(float(line[0]))
                I.append(float(line[1]))

        return keV, I

    # clear text
    def clear_text(self):
        self.output_textbox.configure(state='normal')
        self.output_textbox.delete('0.0','end')
        self.output_textbox.configure(state='disabled')
        
    # update plot
    def plot_spectra(self):
        try:
            y_end = max(self.I)*1.1
            x_end = max(self.keV)*1.1
            file_name = self.display_txt_file
        except:
            x_end = 5;
            y_end = 5;
            file_name = "Input Incident Spectrum"
            
        plt_style.use(['dark_background'])
        params["figure.figsize"] = [7.50, 3.50]
        params["figure.autolayout"] = True
        self.figure = plt_figure(figsize = (7.6,4.2), dpi = 100);
        axes = self.figure.add_subplot(111)
        axes.plot(self.keV,self.I, "b-")
        axes.set_title(f'{file_name}')
        axes.set_xlabel('Energy (keV)', fontsize=11)
        axes.set_ylabel('Intensity (counts)', fontsize=11)
        axes.set_xlim(0, x_end)
        axes.set_ylim([0, y_end])
        chart = FigureCanvasTkAgg(self.figure, master = self.graph_frame)
        chart.get_tk_widget().grid(row=0,column=0,columnspan=2)
    
    # calculate mgd
    def calculate_mgd(self,air_kerma_input,air_kerma,dgn,output_units,number_of_projections):
        if air_kerma_input != 'mGy':
            if air_kerma_input == 'mrad':
                air_kerma = air_kerma * 0.01 # convert from mrad air kerma to mGy
            elif air_kerma_input == 'R':
                air_kerma = air_kerma * 8.77 # convert from R to mGy
            elif air_kerma_input == 'mR':
                air_kerma = air_kerma *  0.00877 # convert from mR to mGy
                
        mgd = air_kerma*dgn*float(number_of_projections) # in mGy/mGy
        
        if output_units == 'mrad':
            mgd = mgd * 100 # converts mgd to mrad
        
        return mgd
    
    # write inputs to textbox
    def output_dose(self,*values):
        
        self.output_textbox.configure(state='normal')
        self.output_textbox.insert("end", f'\n\nMGD = {self.mgd:.4f} {self.output_units.get()}')
        self.output_textbox.insert("end", f' with {self.number_projections_entry.get()} projections')
        self.output_textbox.insert("end", f' with {self.mAs_entry.get()} mAs')

        
        for index in range(len(values)):
            if index == 0 or index%2==0:
                self.output_textbox.insert("end", f'\n{values[index]}')
            else:
                self.output_textbox.insert("end", f'{values[index]}')
                
        self.output_textbox.configure(state='disabled')
        
    # function to calculate dose    
    def calculate_dose(self):
        # get inputs
        current_method = self.method_chosen.get()
        air_kerma_input_units = self.air_kerma_units_combo.get() 
        output_units = self.output_units.get() 
        air_kerma = self.air_kerma_entry.get()
        number_of_projections = self.number_projections_entry.get()
        
        
        try:
            air_kerma_check = len(air_kerma)
            number_of_projections_check = len(number_of_projections)
            air_kerma = float(air_kerma) # check if only numbers
            mAs_per_projection = float(self.mAs_entry.get())
            air_kerma = mAs_per_projection * air_kerma
            
            if air_kerma_check == 0 or number_of_projections_check == 0:
                raise(ValueError)
            
            elif current_method == 2 or current_method==3:
                kev_check = len(self.keV)
                if kev_check == 0:
                    raise(TypeError)
        
            # calculate method based on what is chosen
            if current_method == 1: #Sarno 49 kVp W spectra
                # get parameters
                HVL =  self.HVL_combo.get()
                breast_diameter = self.Breast_diameter_combo.get()
                breast_glandularity = self.Breast_glandularity_combo.get()
                breast_height = ''.join(self.Breast_height_combo.get().split(' ')[0:2])
                
                # calculate dgn for polyenergetic
                dgn_subtable_breast_height = Sarno_poly_dgn.groupby(['breast height']).get_group(breast_height)
                dgn_subtable_glandularity = dgn_subtable_breast_height.groupby(['Glandularity']).get_group(breast_glandularity)
                dgn = dgn_subtable_glandularity.loc[float(HVL), str(breast_diameter)]
                
                # calculate mgd
                self.mgd = self.calculate_mgd(air_kerma_input_units, air_kerma, dgn, output_units,number_of_projections)
                
                self.output_dose('Breast diameter: ', breast_diameter,
                                 'HVL: ', HVL,
                                 'Breast_glandularity: ' , breast_glandularity,
                                 'Breast Height: ', self.Breast_height_combo.get())
                
            elif current_method == 2: # Sarno any spectrum
                breast_diameter = self.Breast_diameter_combo.get()
                breast_glandularity = self.Breast_glandularity_combo.get()
                breast_height = ''.join(self.Breast_height_combo.get().split(' ')[0:2])
                
                # get dgn coefficients
                dgn_subtable_breast_height = Sarno_mono_dgn.groupby(['breast height']).get_group(breast_height)
                dgn_subtable_glandularity = dgn_subtable_breast_height.groupby(['Glandularity']).get_group(breast_glandularity)
                values = dgn_subtable_glandularity[str(breast_diameter)].tolist()
                variables = np.zeros((len(self.keV),len(values)))
                
                for index in range(0,len(values)):
                    variables[:,index] = [float(values[index])]#*len(self.keV)
                
                # calulate dgn 
                dgn = calculate_pDgNct('Sarno Koning',variables,self.keV,self.I) # units of mGy/mGy
                                
                self.mgd = self.calculate_mgd(air_kerma_input_units, air_kerma, dgn, output_units,number_of_projections)
                
                self.output_dose('Breast diameter: ' ,breast_diameter,
                                 'Breast Glandularity: ', breast_glandularity,
                                 'Breast Height: ', self.Breast_height_combo.get())
         
            elif current_method ==3: # Hernandez any spectrum
                # get the VGF and DgN list
                VGF = self.VGF_combo.get().split('=')[0].strip()
                DgN_list = Hernandez_hetero_mono_dgn.loc[:,VGF].tolist()
                
                # index the list to fit keV 
                start_index = int(abs(self.minimum-9))
                if self.maximum != 70:    
                    end_index = int(abs(self.maximum-9))+1
                else:
                    end_index = -1
                
                # interpolate the DgN list if necessary
                Hernandez_keV = list(np.arange(self.minimum,self.maximum+1))
                DgN_list = DgN_list[start_index:end_index]
                interp_DgN_list = np.interp(self.keV,Hernandez_keV,DgN_list)
                
                # get the DgN coefficients in mGy/mGy
                dgn = calculate_pDgNct('Hernandez',interp_DgN_list, self.keV, self.I)
                
                print(dgn)
                
                #print(dgn)
                self.mgd = self.calculate_mgd(air_kerma_input_units, air_kerma, dgn, output_units,number_of_projections)
                
                self.output_dose('VGF: ', self.VGF_combo.get())
            
            else: # Sechopoulos method
                # get parameters
                breast_diameter = self.Breast_diameter_combo.get()
                breast_glandularity = self.Breast_glandularity_combo.get()
                breast_height = float(self.Breast_height_combo.get().split('x')[0]) * float(breast_diameter)
                
                # calculate dgn for polyenergetic
                dgn_subtable_breast_height = Sechopoulos_poly_dgn.groupby(['Chest wall-to-nipple distance']).get_group(breast_height)
                dgn = dgn_subtable_breast_height[breast_glandularity].tolist()[0]
               
                # calculate mgd
                self.mgd = self.calculate_mgd(air_kerma_input_units, air_kerma, dgn, output_units,number_of_projections)
                
                self.output_dose('Breast diameter: ', breast_diameter,
                                 'Breast_glandularity: ' , breast_glandularity,
                                 'Breast Height: ', self.Breast_height_combo.get())
                
        except ValueError: # error in air kerma inputs
            pop_up = customtkinter.CTkToplevel()
            
            if air_kerma_check == 0:
                customtkinter.CTkLabel(pop_up, text='Please enter a numeric value into the air kerma entry box or into \nthe number of projections box', font=('Roman', 12)).pack()
            
            else:
                customtkinter.CTkLabel(pop_up, text='Please enter only numbers into the air kerma and ensure \nthat a numeric value is placed into the number of projections', font=('Roman', 12)).pack()
                
        except TypeError: # error in incident spectrum 
            pop_up = customtkinter.CTkToplevel()
            
            customtkinter.CTkLabel(pop_up, text='Please enter an incident spectrum', font=('Roman', 12)).pack()

#%%% Executable Code
customtkinter.set_appearance_mode("light")
root = customtkinter.CTk()
root.title("BCT Dose Calculator")
CT_dose = Main_Window(root)
root.protocol('WM_DELETE_WINDOW', quit_me)
root.mainloop()





