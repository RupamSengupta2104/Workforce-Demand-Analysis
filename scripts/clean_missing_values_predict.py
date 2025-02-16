import pandas as pd
from sklearn.impute import SimpleImputer

# Load the dataset
file_path = "data/glassdoor_jobs.csv"
df = pd.read_csv(file_path)

# Check missing values before handling
print("📌 Missing Values Before Handling:")
print(df.isnull().sum())

# ✅ Convert salary column to numeric (clean currency symbols and commas)
df["salary_avg_estimate"] = df["salary_avg_estimate"].astype(str).str.replace(r"[^\d.]", "", regex=True)
df["salary_avg_estimate"] = pd.to_numeric(df["salary_avg_estimate"], errors="coerce")

# ✅ Define numerical and categorical columns
num_cols = ["salary_avg_estimate", "company_rating", "career_opportunities_rating",
            "comp_and_benefits_rating", "culture_and_values_rating",
            "senior_management_rating", "work_life_balance_rating"]

cat_cols = ["company_size", "company_founded", "employment_type",
            "industry", "sector", "revenue"]

# ✅ Handle numerical missing values (replace with mean)
num_imputer = SimpleImputer(strategy="mean")
df[num_cols] = num_imputer.fit_transform(df[num_cols])

# ✅ Handle categorical missing values (replace with most frequent)
cat_imputer = SimpleImputer(strategy="most_frequent")
df[cat_cols] = cat_imputer.fit_transform(df[cat_cols])

# ✅ Handle remaining missing values (Fixing `inplace=True` issue)
df["company"] = df["company"].fillna("Unknown")  # Fill missing company names
df["job_description"] = df["job_description"].fillna("No description available")  # Fill missing descriptions
df["salary_estimate_payperiod"] = df["salary_estimate_payperiod"].fillna(df["salary_estimate_payperiod"].mode()[0])  # Use most frequent value

# Check missing values after handling
print("\n📌 Missing Values After Handling:")
print(df.isnull().sum())

# ✅ Save the cleaned dataset
df.to_csv("data/glassdoor_jobs_cleaned_final.csv", index=False)
print("\n✅ Final cleaned dataset saved as 'glassdoor_jobs_cleaned_final.csv'.")
