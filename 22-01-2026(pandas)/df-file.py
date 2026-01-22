import pandas as pd



'''
 nrows: gives the specified number of rows 
 usecols: gives the specific columns
'''

# csv1 = pd.read_csv("data-.csv",nrows=2,usecols=["age"])
csv1 = pd.read_csv("data.csv")

print("CSV","-----------------------------------------------------")
print(csv1)






"""
    
- drops rows with any null value
- axis 1 removes columns
- subset : takes the list of columns and removes rows with null values in those columns keeps rest as NAN 

"""

# print("CSV NULL DROPPED","-----------------------------------------------------")
# print(csv1.dropna())
# print(csv1.dropna(axis=1))
# print(csv1.dropna(subset=["city"]))







'''
- fillna : fills the null value with given values
    -    `vlaue` or `{clounm:value}` 
- ffill() copies the previous value
- bfill() copies the next value

'''

# print("CSV NULL FILLED","-----------------------------------------------------")
# print(csv1.fillna("THIS WAS NULL"))

# print(csv1.fillna({
#     "city":"NOT FOUND",
#     "sales":0
# }))

# print(csv1.ffill())
csv1.bfill()








'''
replace(value to replace, value to replace with)
 - gives new dataframe does not affect the original one unless specified 
 - inplace=True updates modifies the original dataframe
'''

print("CSV REPLACE ","-----------------------------------------------------")

csv1.replace(to_replace=35,value=78,inplace=True)
print(csv1.replace("Riya","Mohit"))








