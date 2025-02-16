import pandas as pd

# Load the dataset
file_path = "data/glassdoor_jobs.csv"  # Ensure the file exists in the 'data/' folder
df = pd.read_csv(file_path)

# Check missing values
print("📌 Missing Values in Each Column:")
print(df.isnull().sum())

# Check data types and non-null values
print("\n📌 Dataset Info:")
print(df.info())
