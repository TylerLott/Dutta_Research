# This script takes the original stress strain .csv and finds the ult stress as well as the corresponding strain value.

# IMPORTS
import pandas as pd

# CONSTANTS
DATA_PATH = "../../Original_Data/Stress_Strain/"
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

print(sr_1.columns)

# avg strain and stress
avg_sr_strain = (sr_max_1['Eng_Strain'] + sr_max_2['Eng_Strain'] + sr_max_3['Eng_Strain'] + sr_max_4['Eng_Strain']) / 4
avg_sr_stress = (sr_max_1[' Eng_Stress (MPa) '] + sr_max_2[' Eng_Stress (MPa) '] + sr_max_3[' Eng_Stress (MPa) '] + sr_max_4[' Eng_Stress (MPa) ']) / 4
print(avg_sr_strain, avg_sr_stress)

# HEAT TREATED
ht_1 = pd.read_csv(DATA_PATH + 'SR_HIP_HT/18-064_RT_SR+HIP+HT.csv')
ht_2 = pd.read_csv(DATA_PATH + 'SR_HIP_HT/18-065_RT_SR+HIP+HT.csv')
ht_3 = pd.read_csv(DATA_PATH + 'SR_HIP_HT/18-068_RT_SR+HIP+HT.csv')
ht_4 = pd.read_csv(DATA_PATH + 'SR_HIP_HT/18-069_RT_SR+HIP+HT.csv')

ht_max_1 = ht_1.max()
ht_max_2 = ht_2.max()
ht_max_3 = ht_3.max()
ht_max_4 = ht_4.max()

# avg strain and stress
avg_ht_strain = (ht_max_1['Eng_Strain'] + ht_max_2['Eng_Strain'] + ht_max_3['Eng_Strain'] + ht_max_4['Eng_Strain']) / 4
avg_ht_stress = (ht_max_1[' Eng_Stress (MPa) '] + ht_max_2[' Eng_Stress (MPa) '] + ht_max_3[' Eng_Stress (MPa) '] + ht_max_4[' Eng_Stress (MPa) ']) / 4
print(avg_ht_strain, avg_ht_stress)

