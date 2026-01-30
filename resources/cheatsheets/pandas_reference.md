# Pandas Quick Reference

Essential Pandas operations for data analysis practicals.

## Importing
```python
import pandas as pd
import numpy as np
```

## Reading Data
```python
# CSV
df = pd.read_csv('file.csv')

# Excel
df = pd.read_excel('file.xlsx')

# JSON
df = pd.read_json('file.json')

# With custom parameters
df = pd.read_csv('file.csv', sep=';', encoding='utf-8', index_col=0)
```

## Basic Information
```python
df.head()              # First 5 rows
df.tail()              # Last 5 rows
df.shape               # (rows, columns)
df.info()              # Data types and non-null counts
df.describe()          # Statistical summary
df.columns             # Column names
df.dtypes              # Data types of each column
```

## Data Selection
```python
# Single column
df['column_name']
df.column_name

# Multiple columns
df[['col1', 'col2']]

# Rows by index
df.iloc[0]             # First row
df.iloc[0:5]           # First 5 rows

# Rows by label
df.loc[0]
df.loc[0:5, 'column']

# Conditional selection
df[df['age'] > 25]
df[(df['age'] > 25) & (df['city'] == 'NYC')]
```

## Data Cleaning
```python
# Check for missing values
df.isnull().sum()
df.isna().sum()

# Drop missing values
df.dropna()                    # Drop rows with any NaN
df.dropna(axis=1)              # Drop columns with any NaN
df.dropna(subset=['col1'])     # Drop rows with NaN in col1

# Fill missing values
df.fillna(0)                   # Fill with 0
df.fillna(df.mean())           # Fill with mean
df.fillna(method='ffill')      # Forward fill
df.fillna(method='bfill')      # Backward fill

# Drop duplicates
df.drop_duplicates()
df.drop_duplicates(subset=['col1'])

# Replace values
df.replace('old', 'new')
df.replace({'col1': {'old': 'new'}})
```

## Data Manipulation
```python
# Add new column
df['new_col'] = df['col1'] + df['col2']
df['new_col'] = df['col1'].apply(lambda x: x * 2)

# Rename columns
df.rename(columns={'old_name': 'new_name'})

# Drop columns
df.drop('column', axis=1)
df.drop(['col1', 'col2'], axis=1)

# Sort
df.sort_values('column')
df.sort_values(['col1', 'col2'], ascending=[True, False])

# Change data type
df['column'] = df['column'].astype(int)
df['date'] = pd.to_datetime(df['date'])
```

## Aggregation
```python
# Basic statistics
df['column'].mean()
df['column'].median()
df['column'].std()
df['column'].min()
df['column'].max()
df['column'].sum()
df['column'].count()

# Group by
df.groupby('category')['value'].mean()
df.groupby(['cat1', 'cat2'])['value'].sum()
df.groupby('category').agg({'col1': 'mean', 'col2': 'sum'})

# Value counts
df['column'].value_counts()
df['column'].value_counts(normalize=True)  # Percentages
```

## Merging and Joining
```python
# Concatenate
pd.concat([df1, df2])                    # Vertically
pd.concat([df1, df2], axis=1)            # Horizontally

# Merge (SQL-style joins)
pd.merge(df1, df2, on='key')             # Inner join
pd.merge(df1, df2, on='key', how='left') # Left join
pd.merge(df1, df2, on='key', how='right')# Right join
pd.merge(df1, df2, on='key', how='outer')# Outer join
```

## String Operations
```python
# String methods (for string columns)
df['column'].str.lower()
df['column'].str.upper()
df['column'].str.strip()
df['column'].str.replace('old', 'new')
df['column'].str.contains('pattern')
df['column'].str.startswith('prefix')
df['column'].str.split(',')
```

## Date/Time Operations
```python
# Convert to datetime
df['date'] = pd.to_datetime(df['date'])

# Extract components
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['dayofweek'] = df['date'].dt.dayofweek

# Time difference
df['date2'] - df['date1']
```

## Export Data
```python
# CSV
df.to_csv('output.csv', index=False)

# Excel
df.to_excel('output.xlsx', index=False)

# JSON
df.to_json('output.json')
```

## Useful Tips
```python
# Chain operations
result = (df
    .dropna()
    .groupby('category')['value']
    .mean()
    .sort_values(ascending=False)
)

# Sample random rows
df.sample(n=10)              # 10 random rows
df.sample(frac=0.1)          # 10% of rows

# Reset index
df.reset_index(drop=True)

# Set index
df.set_index('column')

# Copy dataframe
df_copy = df.copy()
```

## Common Patterns
```python
# Calculate percentage
df['percentage'] = df['value'] / df['value'].sum() * 100

# Categorize values
df['category'] = pd.cut(df['value'], bins=[0, 50, 100], labels=['Low', 'High'])

# Create binary flag
df['is_adult'] = df['age'] >= 18

# Rolling average
df['rolling_avg'] = df['value'].rolling(window=7).mean()
```

## Performance Tips
- Use `df.loc` and `df.iloc` instead of chaining `[]`
- Use vectorized operations instead of loops
- Use `inplace=True` parameter to modify DataFrame without copying
- Use appropriate data types (e.g., 'category' for categorical data)

## More Resources
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [10 Minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Pandas Cheat Sheet (Official)](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
