import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Load the dataset
file_path = "data/glassdoor_jobs_cleaned_final.csv"
df = pd.read_csv(file_path)

# Create output directory for saving images
output_dir = Path("outputs/eda/")
output_dir.mkdir(parents=True, exist_ok=True)

# Summary statistics
summary_stats = df.describe()
print("\n📌 Summary Statistics:")
print(summary_stats)
summary_stats.to_csv(output_dir / "summary_statistics.csv")

# Distribution of company ratings
plt.figure(figsize=(8, 6))
sns.histplot(df["company_rating"].dropna(), bins=20, kde=True)
plt.title("Distribution of Company Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.savefig(output_dir / "company_rating_distribution.png")
plt.show()

# Salary distribution
plt.figure(figsize=(8, 6))
sns.histplot(df["salary_avg_estimate"].dropna(), bins=20, kde=True)
plt.title("Distribution of Salary Estimates")
plt.xlabel("Average Salary Estimate")
plt.ylabel("Count")
plt.savefig(output_dir / "salary_distribution.png")
plt.show()

# Correlation heatmap (only numeric columns)
numeric_cols = df.select_dtypes(include=['number'])
plt.figure(figsize=(10, 6))
corr_matrix = numeric_cols.corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.savefig(output_dir / "correlation_heatmap.png")
plt.show()

print("\n✅ Exploratory Data Analysis Completed. Plots saved in outputs/eda/")
