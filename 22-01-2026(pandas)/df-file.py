import pandas as pd




# nrows: gives the specified number of rows 
# usecols: gives the specific columns

# csv1 = pd.read_csv("data-.csv",nrows=2,usecols=["age"])
csv1 = pd.read_csv("data.csv")

print("CSV","-----------------------------------------------------")
print(csv1)

"""_summary_
    
- drops rows with any null value
- axis 1 removes columns
- subset : takes the list of columns and removes rows with null values in those columns keeps rest as NAN 

"""

print("CSV NULL DROPPED","-----------------------------------------------------")
# print(csv1.dropna())
# print(csv1.dropna(axis=1))

print(csv1.dropna(subset=["city"]))




