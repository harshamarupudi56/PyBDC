# Python Breast Dosage Calculator: PyBDC 1.0
Python toolkit for calculating dosage for breast CT.\
The following software enables accurate dose estimation for one or various breast exposures specifically for breast CT. The software can be used on Windows and Mac operating systems and using a graphical user interface. The mode is further explained below along with an overview of the methods, how to choose a method, the program inputs and buttons, the incident spectrum format, images of the GUI, and the accompanying data files.

Code execution
----------
Clone PyBDC repository.
```
git clone https://github.com/harshamarupudi56/PyBDC.git
```

Run the following commands to install required dependencies.
```
apt-get -y install python3.11-tk
apt-get -y install pip
cd PyBDC
pip install -r requirements.txt
```

The requierd dependencies in [requirements.txt](requirements.txt).
```
customtkinter==5.2.2
matplotlib==3.8.0
numpy==1.26.0
pandas==1.3.4
```

Run PyBDC.
```
python3 professional_modern_ct_dose_3.py
```

User guide
----------
Please refer [User Guide](User_Guide) (Quick Start Guide) to check the workflow of PyBDC.


References
----------
1. Sarno, A., Mettivier, G., Di Lillo, F., & Russo, P. (2017). A Monte Carlo study of monoenergetic and polyenergetic normalized glandular dose (DgN) coefficients in mammography. Physics in medicine and biology, 62(1), 306–325. https://doi.org/10.1088/1361-6560/62/1/306
2. Hernandez, A. M., Becker, A. E., & Boone, J. M. (2019). Updated breast CT dose coefficients (DgNCT ) using patient-derived breast shapes and heterogeneous fibroglandular distributions. Medical physics, 46(3), 1455–1466. https://doi.org/10.1002/mp.13391
3. Sechopoulos, I., Feng, S. S., & D'Orsi, C. J. (2010). Dosimetric characterization of a dedicated breast computed tomography clinical prototype. Medical physics, 37(8), 4110–4120. https://doi.org/10.1118/1.3457331

Disclaimer
----------

This software and documentation was developed at the Food and Drug Administration (FDA) by employees of the Federal Government in the course of their official duties. Pursuant to Title 17, Section 105 of the United States Code, this work is not subject to copyright protection and is in the public domain. Permission is hereby granted, free of charge, to any person obtaining a copy of the Software, to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, or sell copies of the Software or derivatives, and to permit persons to whom the Software is furnished to do so. FDA assumes no responsibility whatsoever for use by other parties of the Software, its source code, documentation or compiled executables, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. Further, use of this code in no way implies endorsement by the FDA or confers any advantage in regulatory decisions. Although this software can be redistributed and/or modified freely, we ask that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified. 


PyBDC: Joseph Manus B.S., Harsha Marupudi, M.Eng., Bahaa Ghammraoui, Ph.D. US Food and Drug Administration, Center for Devices and Radiological Health, Office of Science and Engineering Labs, Division of Imaging, Diagnostics, and Software Reliability.

