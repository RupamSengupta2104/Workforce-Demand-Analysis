import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the categorized job listings data
df = pd.read_csv("data/categorized_job_listings.csv")

# Analyze job demand by industry
industry_counts = df["industry"].value_counts().head(10)  # Top 10 industries

# Analyze job demand by sector
sector_counts = df["sector"].value_counts().head(10)  # Top 10 sectors

# Plot job demand by industry
plt.figure(figsize=(12, 6))
sns.barplot(x=industry_counts.values, y=industry_counts.index, palette="viridis")
plt.xlabel("Number of Job Listings")
plt.ylabel("Industry")
plt.title("Top 10 Industries by Job Demand")
plt.savefig("outputs/industry_demand.png")  # Save plot
plt.show()

# Plot job demand by sector
plt.figure(figsize=(12, 6))
sns.barplot(x=sector_counts.values, y=sector_counts.index, palette="magma")
plt.xlabel("Number of Job Listings")
plt.ylabel("Sector")
plt.title("Top 10 Sectors by Job Demand")
plt.savefig("outputs/sector_demand.png")  # Save plot
plt.show()

# Save industry and sector demand analysis to CSV
industry_counts.to_csv("data/industry_demand_analysis.csv")
sector_counts.to_csv("data/sector_demand_analysis.csv")

print("Industry and sector demand analysis completed and saved!")
