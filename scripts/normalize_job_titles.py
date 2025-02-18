import pandas as pd
import re

# Load the dataset
df = pd.read_csv("data/glassdoor_jobs_cleaned_final.csv")

def normalize_job_title(title):
    """Normalize job titles by converting to lowercase and standardizing common variations."""
    title = title.lower().strip()
    title = re.sub(r'\b(data scientist|data science)\b', 'data scientist', title)
    title = re.sub(r'\b(software engineer|developer|programmer)\b', 'software engineer', title)
    title = re.sub(r'\b(machine learning engineer|ml engineer)\b', 'machine learning engineer', title)
    title = re.sub(r'\b(analyst|business analyst)\b', 'business analyst', title)
    return title

# Apply normalization
df['normalized_job_title'] = df['job_title'].apply(normalize_job_title)

# Save the updated dataset
df.to_csv("data/normalized_job_listings.csv", index=False)

print("✅ Job titles normalized and saved to 'data/normalized_job_listings.csv'")
