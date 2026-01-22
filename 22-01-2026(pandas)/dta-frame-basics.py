import pandas as pd

# --- Create DataFrame ---
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London']
}
df = pd.DataFrame(data)

# --- Inspect Data ---
print(df.head())        # First rows
print(df.info())        # Structure
print(df.describe())    # Stats summary

# --- Select Data ---
print(df['Name'])       # Single column
print(df[['Name','City']]) # Multiple columns
print(df.iloc[0])       # First row
print(df.loc[1,'Age'])  # Specific cell

# --- Add / Modify ---
df['Country'] = ['USA','France','UK']   # New column
df.loc[0,'Age'] = 26                    # Update value

# --- Drop ---
df = df.drop('Country', axis=1)   # Drop column
df = df.drop(2, axis=0)           # Drop row

# --- Filtering ---
print(df[df['Age'] > 28])         # Rows with Age > 28

# --- Grouping ---
print(df.groupby('City')['Age'].mean())

# --- Merge ---
other = pd.DataFrame({'City':['Paris','London'],'Population':[2.1,8.9]})
merged = pd.merge(df, other, on='City')
print(merged)

# --- I/O ---
df.to_csv('output.csv', index=False)    # Save to CSV