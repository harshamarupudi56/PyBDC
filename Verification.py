#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 16:11:52 2024

@author: sriharsha.marupudi
"""
import sys 
import numpy as np  
sys.path.append("/gpfs_projects.sriharsha.marupudi/PCD/Harsha/2023/Storage/January/Dosage_Code/")
# 16 cm, 2xradius, 50%, pdgn = 0.03272299241112477

def exposure_per_fluence(E):
    exposure = np.zeros(len(E))
    for i in range(len(exposure)):
        keV = E[i]
        temp = ((-5.023290717769674e-6 +
                 1.810595449064631e-7 +
                 np.sqrt(keV) + np.log(keV) +
                 0.008838658459816926 / keV**2)**(10**-3)) / 1000 * 0.1145
        exposure[i] = temp
    return exposure


def dgn_calculate(a, b, c, d, e, f, g, h, keVs):
    dgn = np.zeros(len(keVs))
    for i in range(len(keVs)):
        E = keVs[i]
        temp = a * 10**(-14) * E**8 + b * 10**(-12) * E**7 \
             + c * 10**(-10) * E**6 + d * 10**(-8) * E**5 \
             + e * 10**(-6) * E**4 + f * 10**(-4) * E**3 \
             + g * 10**(-3) * E**2 + h * 10**(-2) * E
        dgn[i] = temp
    return dgn



def pDgN_calculate_denominator(I,exposure):
    total = I*exposure 
    pDgN_denom = np.sum(total)

    return pDgN_denom 


def pDgN_calculate_numerator(I,dgn,exposure):
    total = I * exposure * dgn 
    pDgN_num = sum(total)
 
    return pDgN_num 

 
a = -0.41324119391158
b = 4.88540710576677
c = -13.0460380815292
d = 15.3913804609064
e = -9.19621868949206
f = 2.66123817129083
g = -2.67974610124986
h = 0.883219836298924

keV = np.array([10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14])
I = np.array([6.20275e2, 2.26229e2, 5.25667e2, 2.39324e3, 1.45979e3, 2.17293e3, 3.36611e3, 4.89394e3, 6.61405e3])

exposure = exposure_per_fluence(keV)
dgn = dgn_calculate(a, b, c, d, e, f, g, h, keV)

pDgN_num = pDgN_calculate_numerator(I, dgn, exposure)
pDgN_denom = pDgN_calculate_denominator(I, exposure)
pDgN = pDgN_num / pDgN_denom

print("pDgN =", pDgN)

 
