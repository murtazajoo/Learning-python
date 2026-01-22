import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [45, 30, 35],
    'City': ['New York', 'Paris', 'London']
}

df= pd.DataFrame(data,index=["a","b","c"])
print(df)
print()
print(df.columns)
print()

print(df.index)
print()

print(df.shape)
print()

print(df[["Name","Age"]])
print()


print(df.drop("a",axis=0))
print()

df["Country"]="USA"
print(df)
print()


print(df.sort_values("Age",ascending=False))
print()

print(df.sort_values("Age"))
print()

print(df.isna())
print()


print(df[df['Age'] > 38])
print()

#-------------------------------------------------------------------------------------------------------------------------------------

df2 = pd.DataFrame(
    [[1, 'A'], [2, 'B'], [3, 'C']],
    columns=['Number', 'Letter']
)

print(df2)
print()


# View first 5 rows
print(df.head())
print()


# Select a column
print(df["Name"])
print()

# Select multiple columns
print(df[["Name",'Age']])
print()

# Select rows by index
print(df.iloc[0])  # first row
print()

# print(df.loc[1])   # row with index label 1


# Groups rows by City and calculates the average Age for each group
print(df.groupby('City')['Age'].mean())
print()

#-----------------------------------------------------------------------------------------------------------

# making dataframes from series inputs 
sr={"a":pd.Series([1,2,3,4]),
    "b":pd.Series([5,6,7,8])
    }

var=pd.DataFrame(sr)
print(var)
print()

#--------------------------------------------------------------------------------------------------------------

#Arthematic OPerations 


var= pd.DataFrame({"a":pd.Series([1,2,3,4]),
    "b":pd.Series([5,6,7,8])
    })

#addition 
var["c"]=var["a"]+var["b"]
print(var["c"])
print()

#subtraction
var["c"]=var["a"]-var["b"]
print(var["c"])
print()

#Multiplication

var["c"]=var["a"] * var["b"]
print(var["c"])
print()

#divide
var["c"]=var["a"] / var["b"]
print(var["c"])
print()

#dataframe through Tuples 

data = [
    ("Suh", 24, "BCA"),
    ("Mur", 22, "MCA"),
    ("Adil", 26, "BBA")
]

df=pd.DataFrame(data,columns=["Name","Age","Course"])
print(df)


