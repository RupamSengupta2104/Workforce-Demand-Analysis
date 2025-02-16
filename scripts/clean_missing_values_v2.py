import pandas as pd

# Load the dataset
file_path = "data/glassdoor_jobs.csv"  # Ensure the file exists in the 'data/' folder
df = pd.read_csv(file_path)

# Display missing values before cleaning
print("📌 Missing Values Before Cleaning:")
print(df.isnull().sum())

# 1️⃣ Drop rows with too many missing values (more than 40% missing)
row_threshold = int(0.6 * len(df.columns))  # Keep rows with at least 60% non-null values
df = df.dropna(thresh=row_threshold)

# 2️⃣ Drop columns with more than 50% missing values
col_threshold = int(0.5 * len(df))  # Keep columns with at least 50% non-null values
df = df.dropna(axis=1, thresh=col_threshold)

# 3️⃣ Fill missing categorical values using forward-fill and backward-fill
cat_cols = df.select_dtypes(include=["object"]).columns
df[cat_cols] = df[cat_cols].fillna(method="ffill").fillna(method="bfill")

# 4️⃣ Fill remaining missing numerical values with median
num_cols = df.select_dtypes(include=["number"]).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# Display missing values after cleaning
print("\n✅ Missing Values After Cleaning:")
print(df.isnull().sum())

# Save the cleaned dataset
cleaned_file_path = "data/glassdoor_jobs_cleaned_v2.csv"
df.to_csv(cleaned_file_path, index=False)
print(f"\n📁 Cleaned dataset saved as: {cleaned_file_path}")
