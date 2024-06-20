Methods Overview
==================

There are 4 methods available in PyBCD: 

* Sarno 49 kVp W Spectra (Sarno Koning BCT) 

* Sechopoulos 49 kVp Any Spectra (Sechopoulos Koning BCT) 

* Sarno Any Specturm 

* Hernandez Any Spectrum (Hernandez Heterogeneous BCT) 


The Sarno Koning BCT method utilizes the Koning BCT apparatus which houses a 49 kVp W-anode with 1.40 mm Al. Other values are included because of possible variations in Al filter length. Sarno Any Spectrum on the other hand makes use of an incident X-ray spectrum input by the user. The Sarno model represents the breast as a cylinder with a homogoneous mixture of glandular and adipose tisssue. Additonally the model assumes a 1.45 mm thick skin layer and a radiation source placed 650 mm from the isocenter.

Sechopolous method also uses the Koning BCT apparatus. However, the method uses a single HVL value of 1.32 mm Al and models the breast as a semi-ellipsoid with a homogeneous mixture of adipose and glandular tissue.

The Hernandez Heterogeneous BCT method compared to the Sarno methods, models the breast as a heterogeneous mixture of adipose and glandular tissue where the individual tissues voxels are either 100% adipose or 100% glandular. The skin thickness is assumed to be 1.5 mm and the radiation source is placed 650 mm from the isocenter. Rather than being characterized by breast glandularity, this method uses volume glandular fraction or VGF for short. The heterogeneous categories, V1, V3, and V5 are characterized as follows:

V1: Volume Glandular Fraction (VGF) = 19.9%, median volume of 276 cm3, median diameter through the center of 87 mm, and median diameter at the chest wall of 103.4 mm

V3: Volume Glandular Fraction (VGF) = 9.5%, median volume of 616 cm3, median diameter through the center of 106.6 mm, and median diameter at the chest wall of 125.2 mm

V5: Volume Glandular Fraction (VGF) = 3.8%, median volume of 1174 cm3, median diameter through the center of 124.4 mm, and median diameter at the chest wall of 150.4 mm


Choosing a Method
==================
The GUI offers three methods the user can choose from which are Sarno Koning BCT, Sarno Incident Spectrum, and Hernandez Heterogeneous BCT via radio button selection. Next to each method, a radio button can be found that if pressed selects the method. You will note that once pressed, certain buttons and parameters are activated, and others are deactivated. What is activated and deactivated is as follows:

Sarno 49 kVp W Spectra (Sarno Koning BCT) 
* Activated: Breast Diameter, Breast Height, Breast Glandularity, HVL, Air Kerma, Air Kerma units, MGD units, Clear Text, and Calculate Dose
* Deactivated: Heterogeneous Categories, Input Incident Spectrum, and Graph Spectrum
* Assumptions: Cylindrical breats of homogenous composition. Skin layer of 1.45 cm. 65 cm radiation source to isocenter distance. 

Sechopoulos 49 kVp Any Spectra (Sechopoulos Koning BCT) 
* Activated: Breast Diameter, Breast Height, Breast Glandularity, HVL, Air Kerma, Air Kerma units, MGD units, Clear Text, and Calculate Dose
* Deactivated: Heterogeneous Categories, Input Incident Spectrum, and Graph Spectrum 
* Assumptions: Semi-ellipsoidal breast of homogeneous composition. Skin layer of 1.45 mm. 65 cm radiation source to isocenter distance. 

Sarno Any Specturm 
* Activated: Breast Diameter, Breast Height, Breast Glandularity, Air Kerma, Air Kerma units, MGD units, Input Incident Spectrum, Graph Spectrum*, Clear Text, and Calculate Dose
* Deactivated: HVL, Heterogeneous Categories
* Assumptions: Cylindircal brast of homogenous compositon. 65 cm radiatoin source to isocenter distance. 

Hernandez Any Spectrum (Hernandez Heterogeneous BCT) 
* Activated: Heterogeneous Categories, Air Kerma, Air Kerma units, MGD units, Input Incident Spectrum, Graph Spectrum*, Clear Text, and Calculate Dose
* Deactivated: Breast Diameter, Breast Height, Breast Glandularity, HVL
* Assumptions: Real CT breast images were grouped into three volume glandular fraction categories V1, V2, and V3.	Each category of breast assumes a heterogeneous composition.	Skin layer of 1.50 mm. 65 cm radiation source to isocenter distance

Graph spectrum will be activated after a valid text file is entered. If an invalid text file is entered, a popup will appear prompting you to make the necessary changes.
Program Inputs and Buttons 


Program Inputs and Buttons
==========================
Table 1 shows summarizes all the inputs into the program, the format, and the valid ranges. For the program inputs, the parameters other than BCT methods and the Air Kerma can be chosen using the downward arrow button. After clicking the downward arrow, a dropdown menu will appear where you can choose the option of your choice. The BCT method can be chosen via the radio buttons found to the left of the button and the Air Kerma can be manually entered in the box to the right of the parameter. Table 2 summarizes the different buttons and their purpose. These buttons can be simply pressed and the outlined effect in the table will occur. As mentioned above, in the Choosing a Method section, certain buttons will be active and inactive depending on the method chosen.

+---------------------------+-----------------------------------------------------+
| Parameter name            | Input                                               |
+===========================+=====================================================+
| BCT methods               | Sarno Koning BCT                                    |
|                           | Sarno Incident Spectrum                             |
|                           | Hernandez Heterogeneous BCT                         |
+---------------------------+-----------------------------------------------------+
| Breast Diameter (cm)      | 8, 10, 12, 14, 16, 18 (Sarno method)                |
|                           | 10, 12, 14, 16, 18 (Sechopoulos method)             |
+---------------------------+-----------------------------------------------------+
| Breast Height             | 1 x radius                                          |
|                           | 1.5 x radius                                        |
|                           | 2 x radius                                          |
+---------------------------+-----------------------------------------------------+
| Breast Glandularity       | 0.1%, 14.3%, 25%, 50%, 100% (Sarno method)          |
|                           | 1%, 14.3%, 25%, 50%, 100% (Sechopoulos method)      |
+---------------------------+-----------------------------------------------------+
| HVL (mm Al)               | 1.25, 1.30, 1.35, 1.40, 1.45, 1.50                  |
+---------------------------+-----------------------------------------------------+
| Heterogeneous Categories  | V1, V3, V5                                          |
+---------------------------+-----------------------------------------------------+
| Air Kerma                 | any numerical value                                 |
+---------------------------+-----------------------------------------------------+
| Air Kerma Units           | R, mGy, mrad                                        |
+---------------------------+-----------------------------------------------------+
| MGD Units                 | mGy, mrad                                           |
+---------------------------+-----------------------------------------------------+


Table 1. Summary of parameters and their inputs.


+----------------------+------------------------------------------------------------------+
| Button               | Function                                                         |
+======================+==================================================================+
| Input Incident       | Opens file prompt where you select your input incident file.     |
| Spectrum             | The GUI will then read the input file and pull the keV and       |
|                      | counts from the file. It further prints the shortened file onto  |
|                      | the text box.                                                    |
+----------------------+------------------------------------------------------------------+
| Graph Spectrum       | Graphs the inputted spectrum.                                    |
+----------------------+------------------------------------------------------------------+
| Clear Text           | Clears the text box.                                             |
+----------------------+------------------------------------------------------------------+
| Calculate Dose       | After filling all the necessary parameters, pressing this        |
|                      | button will calculate and display the estimated mean glandular   |
|                      | dose along with the selected values of the parameters.           |
+----------------------+------------------------------------------------------------------+

Table 2. Summary of Buttons and their functions.

The chosen incident spectrum file must have a specific format which differs for the method chosen. This format is further elucidated in the Incident Spectrum Format section found below.

Incident Spectrum Format
========================

First, the incident spectrum must be saved in a text file (typically a ‘.txt’ file but any text file format is accepted) and it can have any name (there is no naming convention). Next, the text file inputs must be in the form of two columns where the keV is the first column and the counts is the second column. It should be noted that keV uses a step size of 0.5. Any step size can be used. The Hernandez Heterogeneous BCT DgN coefficients are interpolated to fit any step size.
 
Furthermore, Sarno Incident Spectrum and Hernandez Heterogeneous BCT take different ranges of values. Sarno Incident Spectrum uses a keV range of 8-80 keV inclusive. Hernandez Heterogeneous BCT, on the other hand, uses a range of 7-90 keV inclusive.
