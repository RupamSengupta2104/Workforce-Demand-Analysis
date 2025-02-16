import pandas as pd

# Load dataset
file_path = "data/glassdoor_jobs.csv"
df = pd.read_csv(file_path)

# Check missing values before cleaning
print("📌 Missing Values Before Cleaning:")
print(df.isnull().sum())

# Fill numerical columns with mean
num_cols = df.select_dtypes(include=["number"]).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

# Fill categorical columns with mode
cat_cols = df.select_dtypes(include=["object"]).columns
df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

# Check missing values after cleaning
print("\n✅ Missing Values After Cleaning:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("data/glassdoor_jobs_cleaned_basic.csv", index=False)
print("\n📁 Cleaned dataset saved as: data/glassdoor_jobs_cleaned_basic.csv")
