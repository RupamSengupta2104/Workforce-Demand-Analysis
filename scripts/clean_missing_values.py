import pandas as pd

# Load the dataset
file_path = "data/glassdoor_jobs.csv"  # Ensure the file exists in the 'data/' folder
df = pd.read_csv(file_path)

# Display missing values before cleaning
print("📌 Missing Values Before Cleaning:")
print(df.isnull().sum())

# Strategy to handle missing values

## 1️⃣ Fill missing numerical values with the column mean
num_cols = df.select_dtypes(include=["number"]).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

## 2️⃣ Fill missing categorical values with the mode (most frequent value)
cat_cols = df.select_dtypes(include=["object"]).columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])  # Fill with the most frequent value

# Display missing values after cleaning
print("\n✅ Missing Values After Cleaning:")
print(df.isnull().sum())

# Save the cleaned dataset
cleaned_file_path = "data/glassdoor_jobs_cleaned.csv"
df.to_csv(cleaned_file_path, index=False)
print(f"\n📁 Cleaned dataset saved as: {cleaned_file_path}")
