import pandas as pd

# Load dataset
file_path = "data/glassdoor_jobs.csv"
df = pd.read_csv(file_path)

# Check missing values before cleaning
print("📌 Missing Values Before Cleaning:")
print(df.isnull().sum())

# Drop rows with more than 40% missing values
row_threshold = int(0.6 * len(df.columns))
df = df.dropna(thresh=row_threshold)

# Drop columns with more than 50% missing values
col_threshold = int(0.5 * len(df))
df = df.dropna(axis=1, thresh=col_threshold)

# Forward-fill and backward-fill for categorical columns
cat_cols = df.select_dtypes(include=["object"]).columns
df[cat_cols] = df[cat_cols].fillna(method="ffill").fillna(method="bfill")

# Fill numerical columns with median
num_cols = df.select_dtypes(include=["number"]).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# Check missing values after cleaning
print("\n✅ Missing Values After Cleaning:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("data/glassdoor_jobs_cleaned_ffill_bfill.csv", index=False)
print("\n📁 Cleaned dataset saved as: data/glassdoor_jobs_cleaned_ffill_bfill.csv")
