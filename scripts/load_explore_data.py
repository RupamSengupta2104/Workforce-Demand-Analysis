import pandas as pd

# Define file path directly (without pathlib)
file_path = "data/glassdoor_jobs.csv"  # Ensure the file exists in the 'data/' folder

# Load the dataset
df = pd.read_csv(file_path)

print("\n📌 Column Names in Dataset:")
print(df.columns)

# Display first few rows
print("📌 First 5 rows of the dataset:")
print(df.head())

# Check basic dataset info
print("\n📌 Dataset Info:")
print(df.info())

# Check missing values
print("\n📌 Missing Values in Each Column:")
print(df.isnull().sum())

# Get number of rows and columns
print("\n📌 Dataset Shape (Rows, Columns):", df.shape)

# Get summary statistics for numerical columns
print("\n📌 Summary Statistics:")
print(df.describe())

# Check unique job titles (Adjust column name if different)
print("\n📌 Unique Job Titles:")
print(df["job_title"].unique()[:10])  # Show first 10 unique job titles

# Count job postings by company (Adjust column name if different)
print("\n📌 Top 10 Companies with Most Job Postings:")
print(df["company"].value_counts().head(10))
