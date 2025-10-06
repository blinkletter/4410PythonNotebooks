### IMPORTANT: RUN THIS CODE BLOCK TO LOAD THE INTERPOLATION LIBRARY

###################################################
### Interpolator Functions
###################################################



###################################################
### Create Interpolation Function for H0 from %H2SO4 from Tickle
###################################################

### This function below could be in an external library that you call in your own program.

import pandas as pd
import numpy as np
from scipy.interpolate import make_smoothing_spline               # A function for interpolating a plot using a Bspline algorithm. Returns an interpolation function.

#github_location = "https://raw.githubusercontent.com/blinkletter/4410PythonNotebooks/main/Class_30/data/"
github_location = "./data/"






def MakeInterpolationFunctionForH0inH2SO4byPercentWt():
    Data_File_Name = "02_H0_H2SO4_Tickle_1970.csv"

    Filename = github_location + Data_File_Name
    
    df = pd.read_csv(Filename, 
                     delimiter = ",", 
                     skipinitialspace=True, 
                     comment = "#") 
    
    x = df["%H2SO4"]
    y = df["H0"]
    
    interpolation = make_smoothing_spline(x, y,      ### The x and y data
                                          w=None,    ### A list of weights for each point (default = None)
                                          lam=5)   ### A factor for the degree of smoothing. Change this to change the smoothness.
    
    return(interpolation)


###################################################
### Create Interpolation Function for %H2SO4 from H0 from Tickle
###################################################

# This is the same as above but gets %H2SO4 from H0

def MakeInterpolationFunctionForH2SO4byPercentWtinH0():
    Data_File_Name = "02_H0_H2SO4_Tickle_1970.csv"

    Filename = github_location + Data_File_Name
    
    df = pd.read_csv(Filename, 
                     delimiter = ",", 
                     skipinitialspace=True, 
                     comment = "#") 
    df_sorted = df.sort_values(by="H0", ascending=True) # interpolator required x-axis to be accending in order to work
    y = df_sorted["%H2SO4"]
    x = df_sorted["H0"]
    
    interpolation = make_smoothing_spline(x, y,      ### The x and y data
                                          w=None,    ### A list of weights for each point (default = None)
                                          lam=5)   ### A factor for the degree of smoothing. Change this to change the smoothness.
    
    return(interpolation)


###################################################
### Create Interpolation Function for HR from %H2SO4
###################################################

### This function below could be in an external library that you call in your own program.

def MakeInterpolationFunctionForHRinH2SO4byPercentWt():
    Data_File_Name = "04_Deno_1955_HR_Values.csv"
#    Data_File_Name = "04_Cook_1975_HR_Values.csv"

    Filename = github_location + Data_File_Name
    
    df = pd.read_csv(Filename, 
                     delimiter = ",", 
                     skipinitialspace=True, 
                     comment = "#") 
    
    
    x = df["%H2SO4"]
    y = df["HR"]
    
    interpolation = make_smoothing_spline(x, y,      ### The x and y data
                                          w=None,    ### A list of weights for each point (default = None)
                                          lam=0.1)  ### A factor for the degree of smoothing. Change this to change the smoothness.
    
    return(interpolation)


###################################################
### Create Interpolation Function for a_H2O by X_H2SO4
###################################################

# The activity of water in 0.01 mole fraction H2SO4 is 0.983

### This function below could be in an external library that you call in your own program.

def MakeInterpolationFunctionForH2OActivityinH2SO4byMoleFraction():
    Data_File_Name = "01_Giauque_Table9_activityH2OinH2SO4.csv"
    
    molwtH2SO4 = 98.08; molwtH20 = 18.0; densityH2SO4 = 1.83; densityH2O = 1.000
    
    Filename = github_location + Data_File_Name
    
    df1 = pd.read_csv(Filename, 
                     delimiter = ",", 
                     skipinitialspace=True, 
                     comment = "#") 
    
    molal = df1["conc H2SO4 / m"]
    mass_add_to_1_kg_water = molal * molwtH2SO4
    total_mass_solution = mass_add_to_1_kg_water + 1000
    percent_H2SO4 = mass_add_to_1_kg_water / total_mass_solution * 100
    
    df1["%H2SO4"] = percent_H2SO4
    df1["mole fraction"] = molal / (molal + 1000/molwtH20)
    
    x = df1["mole fraction"]
    y = df1["aH2O"]


    
    interpolation = make_smoothing_spline(x, y,      ### The x and y data
                                          w=None,    ### A list of weights for each point (default = None)
                                          lam=5)     ### A factor for the degree of smoothing. Change this to change the smoothness.
    
    return(interpolation)

def DataForInterpolateH2OActivitybyPercentWtH2SO4():
    Data_File_Name = "01_Giauque_Table9_activityH2OinH2SO4.csv"
    
    molwtH2SO4 = 98.08; molwtH20 = 18.0; densityH2SO4 = 1.83; densityH2O = 1.000
    
    Filename = github_location + Data_File_Name
    
    df1 = pd.read_csv(Filename, 
                     delimiter = ",", 
                     skipinitialspace=True, 
                     comment = "#") 
    
    molal = df1["conc H2SO4 / m"]
    mass_add_to_1_kg_water = molal * molwtH2SO4
    total_mass_solution = mass_add_to_1_kg_water + 1000
    percent_H2SO4 = mass_add_to_1_kg_water / total_mass_solution * 100
    
    df1["%H2SO4"] = percent_H2SO4
    
    x = df1["%H2SO4"]
    y = df1["aH2O"]
    
    return(x,y)

###################################################
### Create Interpolation Function for a_H2O by % H2SO4
###################################################

# The activity of water in 10% H2SO4 is 0.956

### This function below could be in an external library that you call in your own program.

def MakeInterpolationFunctionForH2OActivityinH2SO4byPercentWt():


    Data_File_Name = "01_Giauque_Table9_activityH2OinH2SO4.csv"

    molwtH2SO4 = 98.08; molwtH20 = 18.0; densityH2SO4 = 1.83; densityH2O = 1.000
    
    Filename = github_location + Data_File_Name
    
    df1 = pd.read_csv(Filename, 
                     delimiter = ",", 
                     skipinitialspace=True, 
                     comment = "#") 
    
    molal = df1["conc H2SO4 / m"]
    mass_add_to_1_kg_water = molal * molwtH2SO4
    total_mass_solution = mass_add_to_1_kg_water + 1000
    percent_H2SO4 = mass_add_to_1_kg_water / total_mass_solution * 100
    
    df1["%H2SO4"] = percent_H2SO4
    df1["mole fraction"] = molal / (molal + 1000/molwtH20)

    x = df1["%H2SO4"]
    y = df1["aH2O"]
    
    interpolation = make_smoothing_spline(x, y,      ### The x and y data
                                          w=None,    ### A list of weights for each point (default = None)
                                          lam=10)  ### A factor for the degree of smoothing. Change this to change the smoothness.
    
    return(interpolation)


###################################################
### Create Interpolation Function for Density from %H2SO4
###################################################

# The Density of 100% H2SO4 is 1.831

### This function below could be in an external library that you call in your own program.

def MakeInterpolationFunctionForDensityofH2SO4byPercentWt():
    Data_File_Name = "03_H2SO4_PercentWt_to_MolarConc_CRC.csv"

    Filename = github_location + Data_File_Name
    
    df = pd.read_csv(Filename, 
                     delimiter = ",", 
                     skipinitialspace=True, 
                     comment = "#") 
    
    y = df['Density']
    x = df['%H2SO4']
    
    interpolation = make_smoothing_spline(x, y,     ### The x and y data
                                          w=None,   ### A list of weights for each point (default = None)
                                          lam=5)  ### A factor for the degree of smoothing. Change this to change the smoothness.

    return(interpolation)


###################################################
### Create Interpolation Function for Density from %H2SO4
###################################################

# The Density of 100% H2SO4 is 1.831

### This function below could be in an external library that you call in your own program.

def MakeInterpolationFunctionForH2SO4byPercentWtbyMolarConc():
    Data_File_Name = "03_H2SO4_PercentWt_to_MolarConc_CRC.csv"

    Filename = github_location + Data_File_Name
    
    df = pd.read_csv(Filename, 
                     delimiter = ",", 
                     skipinitialspace=True, 
                     comment = "#") 
    
    x = df['mol/L']
    y = df['%H2SO4']
    
    interpolation = make_smoothing_spline(x, y,     ### The x and y data
                                          w=None,   ### A list of weights for each point (default = None)
                                          lam=5)  ### A factor for the degree of smoothing. Change this to change the smoothness.

    return(interpolation)


###################################################
### Create Interpolation Function for %H2SO4 from Molarity
###################################################

# The Density of 100% H2SO4 is 1.831

### This function below could be in an external library that you call in your own program.

def MakeInterpolationFunctionMolarToH2SO4byPercentWt():
    Data_File_Name = "03_H2SO4_PercentWt_to_MolarConc_CRC.csv"

    Filename = github_location + Data_File_Name
    
    df = pd.read_csv(Filename, 
                     delimiter = ",", 
                     skipinitialspace=True, 
                     comment = "#") 
    
    x = df['mol/L']
    y = df['%H2SO4']
    
    interpolation = make_smoothing_spline(x, y,     ### The x and y data
                                          w=None,   ### A list of weights for each point (default = None)
                                          lam=5)  ### A factor for the degree of smoothing. Change this to change the smoothness.

    return(interpolation)




###################################################
### Switcher function
###################################################


# This code runs only in python 3.10 or above versions
def select_interpolator(parameter):
    match parameter:
        case "H0":
            return MakeInterpolationFunctionForH0inH2SO4byPercentWt()
        case "HR":
            return MakeInterpolationFunctionForHRinH2SO4byPercentWt()
        case "aH2O":
            return MakeInterpolationFunctionForH2OActivityinH2SO4byPercentWt()
        case "Density":
            return MakeInterpolationFunctionForDensityofH2SO4byPercentWt()
        case default:
            return "FAIL"
