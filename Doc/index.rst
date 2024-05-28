Welcome to PyBDC Documentation!
=====================================

Python toolkit for calculating dosage for breast CT.\
The following software enables accurate dose estimation for one or various breast exposures specifically for breast CT. The software can be used on Windows and Mac operating systems and using a graphical user interface. The mode is further explained below along with an overview of the methods, how to choose a method, the program inputs and buttons, the incident spectrum format, images of the GUI, and the accompanying data files.


Table of Contents
==================
.. toctree::
   :hidden:

   Home <self>

.. toctree::
   :maxdepth: 2

   install
   methods
   gui

   examples

Methods Overview 
==================

Currently supports the following plugins:

* Sarno Any Spectrum
* Hernandez Any Spectrum
* Sarno 49 kVp W Spectra
* Sechopoulus 49 kvP W Spectra 

Detailed descriptions on individual methods are provided in section :ref:`methodsoverview`.

Installation
==================
**Clone PyBDC repository** 

git clone https://github.com/harshamarupudi56/PyBDC.git

**Run the following commands to install required dependencies** 

apt-get -y install python3.11-tk
apt-get -y install pip
cd PyBDC
pip install -r requirements.txt

**The required dependencies located in requirements.txt** 

customtkinter==5.2.2
matplotlib==3.8.0
numpy==1.26.0
pandas==1.3.4

**Run PyBDC**

python3 professional_modern_ct_dose_3.py


**PyBDC Team:**
Harsha Marupudi, Jospeh Manus, Bahaa Ghammraoui 

**Citations:**

Sarno, A., Mettivier, G., Di Lillo, F., & Russo, P. (2017). A Monte Carlo study of monoenergetic and polyenergetic normalized glandular dose (DgN) coefficients in mammography. Physics in medicine and biology, 62(1), 306–325. https://doi.org/10.1088/1361-6560/62/1/306

Hernandez, A. M., Becker, A. E., & Boone, J. M. (2019). Updated breast CT dose coefficients (DgNCT ) using patient-derived breast shapes and heterogeneous fibroglandular distributions. Medical physics, 46(3), 1455–1466. https://doi.org/10.1002/mp.13391

Sechopoulos, I., Feng, S. S., & D'Orsi, C. J. (2010). Dosimetric characterization of a dedicated breast computed tomography clinical prototype. Medical physics, 37(8), 4110–4120. https://doi.org/10.1118/1.3457331
