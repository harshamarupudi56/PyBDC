Welcome to PyBDC Documentation!
=====================================

Python toolkit for calculating mean glandular dose for breast CT.
The following software enables accurate breast dosage estimations based on four different models from well published papers. The software can be used on Windows, Mac, and Linux through the use of a Python based GUI. The different methods along with the input parameters are explained in this documentation. The purpose of this tool is to allow breast CT reseachers, medical physicists, and developers a simple method for comapring the dosage between different CT systems to ensure substantial equivalence. 

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

Methods Overview 
==================

Currently supports the following breast models:

* Sarno Any Spectrum

* Hernandez Any Spectrum

* Sarno 49 kVp W Spectra

* Sechopoulus 49 kvP W Spectra 

Detailed descriptions on individual methods are provided in section :ref:`Methods Overview`.

**PyBDC Team:**

Harsha Marupudi, Jospeh Manus, Bahaa Ghammraoui 


**License**

BSD 3-Clause License

Copyright (c) 2023, Harsha Marupudi, Joseph Manus, Bahaa Ghammraoui 
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


**Disclaimer**

This software and documentation was developed at the Food and Drug Administration (FDA) by employees of the Federal Government in the course of their official duties. Pursuant to Title 17, Section 105 of the United States Code, this work is not subject to copyright protection and is in the public domain. Permission is hereby granted, free of charge, to any person obtaining a copy of the Software, to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, or sell copies of the Software or derivatives, and to permit persons to whom the Software is furnished to do so. FDA assumes no responsibility whatsoever for use by other parties of the Software, its source code, documentation or compiled executables, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. Further, use of this code in no way implies endorsement by the FDA or confers any advantage in regulatory decisions. Although this software can be redistributed and/or modified freely, we ask that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.


**Citations:**

Sarno, A., Mettivier, G., Di Lillo, F., & Russo, P. (2017). A Monte Carlo study of monoenergetic and polyenergetic normalized glandular dose (DgN) coefficients in mammography. Physics in medicine and biology, 62(1), 306–325. https://doi.org/10.1088/1361-6560/62/1/306

Hernandez, A. M., Becker, A. E., & Boone, J. M. (2019). Updated breast CT dose coefficients (DgNCT ) using patient-derived breast shapes and heterogeneous fibroglandular distributions. Medical physics, 46(3), 1455–1466. https://doi.org/10.1002/mp.13391

Sechopoulos, I., Feng, S. S., & D'Orsi, C. J. (2010). Dosimetric characterization of a dedicated breast computed tomography clinical prototype. Medical physics, 37(8), 4110–4120. https://doi.org/10.1118/1.3457331
