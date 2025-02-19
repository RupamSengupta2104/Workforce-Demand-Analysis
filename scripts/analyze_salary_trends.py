import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the categorized job listings data
df = pd.read_csv("data/categorized_job_listings.csv")

# Drop rows with missing salary values
df = df.dropna(subset=["salary_avg_estimate"])

# Convert salary to numeric
if df["salary_avg_estimate"].dtype == 'object':
    df["salary_avg_estimate"] = df["salary_avg_estimate"].str.replace(",", "").astype(float)

# Analyze salary trends by industry
industry_salary = df.groupby("industry")["salary_avg_estimate"].median().sort_values(ascending=False).head(10)

# Analyze salary trends by sector
sector_salary = df.groupby("sector")["salary_avg_estimate"].median().sort_values(ascending=False).head(10)

# Plot salary distribution by industry
plt.figure(figsize=(12, 6))
sns.barplot(x=industry_salary.values, y=industry_salary.index, palette="coolwarm")
plt.xlabel("Median Salary ($)")
plt.ylabel("Industry")
plt.title("Top 10 Industries by Median Salary")
plt.savefig("outputs/industry_salary.png")  # Save plot
plt.show()

# Plot salary distribution by sector
plt.figure(figsize=(12, 6))
sns.barplot(x=sector_salary.values, y=sector_salary.index, palette="crest")
plt.xlabel("Median Salary ($)")
plt.ylabel("Sector")
plt.title("Top 10 Sectors by Median Salary")
plt.savefig("outputs/sector_salary.png")  # Save plot
plt.show()

# Save salary analysis results
industry_salary.to_csv("data/industry_salary_analysis.csv")
sector_salary.to_csv("data/sector_salary_analysis.csv")

print("Salary analysis completed and saved!")
