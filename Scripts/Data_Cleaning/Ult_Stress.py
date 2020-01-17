# This script takes the original stress strain .csv and finds the ult stress as well as the corresponding strain value.
# This also averages the values and finds the standard deviation between points

# IMPORTS
import pandas as pd
import numpy as np

# CONSTANTS
DATA_PATH = "../../../Data/Original_Data/Stress_Strain/"
SAVE_PATH = ""

# SR ONLY
sr_1 = pd.read_csv(DATA_PATH + 'SR/18-321_RT_SRonly.csv')
sr_2 = pd.read_csv(DATA_PATH + 'SR/18-322_RT_SRonly.csv')
sr_3 = pd.read_csv(DATA_PATH + 'SR/18-325_RT_SRonly.csv')
sr_4 = pd.read_csv(DATA_PATH + 'SR/18-326_RT_SRonly.csv')

sr_max_1 = sr_1.max()
sr_max_2 = sr_2.max()
sr_max_3 = sr_3.max()
sr_max_4 = sr_4.max()

# avg strain and stress
avg_sr_strain = (sr_max_1['Eng_Strain'] + sr_max_2['Eng_Strain'] + sr_max_3['Eng_Strain'] + sr_max_4['Eng_Strain']) / 4
avg_sr_stress = (sr_max_1[' Eng_Stress (MPa) '] + sr_max_2[' Eng_Stress (MPa) '] + sr_max_3[' Eng_Stress (MPa) '] + sr_max_4[' Eng_Stress (MPa) ']) / 4

print("avg strain sr:" + str(avg_sr_strain))
print("avg stress sr:" + str(avg_sr_stress))

# standard deviations
max_sr_points = [sr_max_1, sr_max_2, sr_max_3, sr_max_4]

strain_sigma = 0
for maxes in max_sr_points:
    strain_sigma += np.power((maxes['Eng_Strain'] - avg_sr_strain), 2)

std_dev_sr_strain = np.sqrt(strain_sigma / (len(max_sr_points)))

stress_sigma = 0
for maxes in max_sr_points:
    stress_sigma += np.power((maxes[' Eng_Stress (MPa) '] - avg_sr_stress), 2)

std_dev_sr_stress = np.sqrt(stress_sigma / (len(max_sr_points)))

print("std dev strain sr:" + str(std_dev_sr_strain))
print("std dev stress sr:" + str(std_dev_sr_stress))


# HEAT TREATED
# ht_1 is an outlier
# ht_1 = pd.read_csv(DATA_PATH + 'SR_HIP_HT/18-064_RT_SR+HIP+HT.csv')
ht_2 = pd.read_csv(DATA_PATH + 'SR_HIP_HT/18-065_RT_SR+HIP+HT.csv')
ht_3 = pd.read_csv(DATA_PATH + 'SR_HIP_HT/18-068_RT_SR+HIP+HT.csv')
ht_4 = pd.read_csv(DATA_PATH + 'SR_HIP_HT/18-069_RT_SR+HIP+HT.csv')

# ht_max_1 = ht_1.max()
ht_max_2 = ht_2.max()
ht_max_3 = ht_3.max()
ht_max_4 = ht_4.max()

# print(ht_max_2, ht_max_3, ht_max_4)

# avg strain and stress
avg_ht_strain = (ht_max_2['Eng_Strain'] + ht_max_3['Eng_Strain'] + ht_max_4['Eng_Strain']) / 3
avg_ht_stress = (ht_max_2[' Eng_Stress (MPa) '] + ht_max_3[' Eng_Stress (MPa) '] + ht_max_4[' Eng_Stress (MPa) ']) / 3

print("avg strain ht:" + str(avg_ht_strain))
print("avg strain ht:" + str(avg_ht_stress))

# standard deviations
max_ht_points = [ht_max_2, ht_max_3, ht_max_4]

strain_sigma = 0
for maxes in max_ht_points:
    strain_sigma += np.power((maxes['Eng_Strain'] - avg_ht_strain), 2)

std_dev_ht_strain = np.sqrt(strain_sigma / (len(max_ht_points)))

stress_sigma = 0
for maxes in max_ht_points:
    stress_sigma += np.power((maxes[' Eng_Stress (MPa) '] - avg_ht_stress), 2)

std_dev_ht_stress = np.sqrt(stress_sigma / (len(max_ht_points)))

print("std dev strain ht:" + str(std_dev_ht_strain))
print("std dev strain ht:" + str(std_dev_ht_stress))





