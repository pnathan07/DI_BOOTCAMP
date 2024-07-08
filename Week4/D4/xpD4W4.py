##Exercice1
import pandas as pd
from sqlalchemy import create_engine

# Read the CSV file
df = pd.read_csv('Uncleaned_DS_jobs.csv')

# Connect to PostgreSQL
username = 'your_username'
password = 'your_password'
hostname = 'your_hostname'
database_name = 'your_database_name'
engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{hostname}/{database_name}')

# Load the original DataFrame into PostgreSQL
table_name = 'your_table_name'
df.to_sql(table_name, engine, if_exists='replace', index=False)

# Identify and remove irrelevant columns
print(df.columns)
columns_to_drop = ['column_name1', 'column_name2']  # Replace with actual column names to drop
df_cleaned = df.drop(columns=columns_to_drop)

# Check for and remove duplicate rows
duplicate_rows = df_cleaned.duplicated()
print(f"Number of duplicate rows: {duplicate_rows.sum()}")
df_cleaned = df_cleaned.drop_duplicates()

# Load the cleaned DataFrame into PostgreSQL
df_cleaned.to_sql(table_name, engine, if_exists='replace', index=False)

##Exercice 2 
import pandas as pd
from sqlalchemy import create_engine

# Load the dataset
df = pd.read_csv('Uncleaned_DS_jobs.csv')

# Standardize column names to lowercase and replace spaces with underscores
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Correct any specific formatting errors if known
# Example: if there are known issues in specific columns, handle them here
# df['some_column'] = df['some_column'].apply(lambda x: x.strip() if isinstance(x, str) else x)
# Display data types of columns
print(df.dtypes)

# Convert columns to appropriate data types
# Example: Convert date columns to datetime
# df['date_column'] = pd.to_datetime(df['date_column'])

# Example: Convert numeric columns to numeric types
# df['numeric_column'] = pd.to_numeric(df['numeric_column'], errors='coerce')

# You can automate type conversion if you have a large number of columns to handle:
for column in df.columns:
    if 'date' in column:
        df[column] = pd.to_datetime(df[column], errors='coerce')
    elif 'id' in column or 'count' in column or 'number' in column:
        df[column] = pd.to_numeric(df[column], errors='coerce')
# Identify missing values
missing_values = df.isnull().sum()
print("Missing values in each column:")
print(missing_values)

# Handle missing values appropriately
# Example: Fill numeric columns with the mean
numeric_columns = df.select_dtypes(include=['number']).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# Example: Fill categorical columns with the mode
categorical_columns = df.select_dtypes(include=['object']).columns
df[categorical_columns] = df[categorical_columns].apply(lambda x: x.fillna(x.mode()[0]))

# Alternatively, drop rows with missing values
# df = df.dropna()

# Or use domain-specific logic for filling missing values
# Example:
# df['some_column'] = df['some_column'].fillna('default_value')
# Connect to PostgreSQL
username = 'your_username'
password = 'your_password'
hostname = 'your_hostname'
database_name = 'your_database_name'
engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{hostname}/{database_name}')

# Load the cleaned DataFrame into PostgreSQL
table_name = 'your_cleaned_table_name'
df.to_sql(table_name, engine, if_exists='replace', index=False)

##Exercice 3 
#ELECT e.employee_id, e.first_name, e.last_name, d.department_name
#FROM employees e
#LEFT JOIN departments d ON e.department_id = d.department_id
#WHERE d.department_id IS NULL;
# Employees without assigned departments
#SELECT e.employee_id, e.first_name, e.last_name, d.department_name
#FROM employees e
#LEFT JOIN departments d ON e.department_id = d.department_id
#WHERE d.department_id IS NULL

#UNION ALL

#-- Departments without any employees
#SELECT NULL AS employee_id, NULL AS first_name, NULL AS last_name, d.department_name
#FROM departments d
#LEFT JOIN employees e ON d.department_id = e.department_id
#WHERE e.employee_id IS NULL;

#Exercice 4
#SELECT e.*, d.*
#FROM employees e
#FULL JOIN departments d ON e.department_id = d.department_id;


 