import pandas as pd 
import numpy as np


#info: uncomment the print statement one by one under =========

#######################################################################################
# panal data - python data analysis
# Pandas is an open-source Python library used for data manipulation, analysis and cleaning. It provides fast and flexible tools to work with tabular data, similar to spreadsheets or SQL tables.
######################################################################################



# series - 1D labled array - a column in excel

# series of single value
# adding indexes the value will be defaulted to 12

s = pd.Series(12,index=[1,2,3,45]) 
# ===========================
# print("Pandas Series: ", s)

s2 = pd.Series(12,index=[1,2,3,4,5,6]) 
# =====================
# print(s+s2) #adds the two series but will replace missing values with ```NAN```

data = np.array([10,20,30,40,50]) 

# index : used to change the index of the series
# dtype: chages th datatype of series
# name : assigns the name to the Series

s = pd.Series(data,index=['g', 'e', 'e', 'k', 's'],dtype="float",name="STUDENTS") 
# ===========================
print("Pandas Series:\n", s,"\n")



# data2 = {"name":"Helllo","age":30}
# s2 = pd.Series(data2) 
# ===========================
# print("Pandas Series:\n", s2,"\n")