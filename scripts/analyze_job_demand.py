import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the categorized dataset
df = pd.read_csv("data/categorized_job_listings.csv")

# Count job listings per category
job_demand = df["Job Category"].value_counts()

# Plot job demand
plt.figure(figsize=(12, 6))
sns.barplot(x=job_demand.index, y=job_demand.values, palette="viridis")
plt.xticks(rotation=45, ha='right')
plt.xlabel("Job Category")
plt.ylabel("Number of Job Listings")
plt.title("Job Demand by Category")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save and show the plot
plt.savefig("outputs/job_demand_by_category.png", bbox_inches='tight')
plt.show()

print("Job demand analysis completed. Plot saved as 'job_demand_by_category.png'.")
