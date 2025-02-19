import pandas as pd

# Load the normalized data
df = pd.read_csv("data/normalized_job_listings.csv")

# Debugging Step: Print column names
print("Columns in the dataset:", df.columns)

# Ensure column name consistency
df.columns = df.columns.str.strip()  # Remove any leading/trailing spaces

# Check if 'job_title' column exists
if "job_title" not in df.columns:
    raise KeyError("The column 'job_title' is missing in the dataset. Check the CSV structure.")

# Define job categories based on keywords
job_categories = {
    "Data Science & AI": ["Data Scientist", "Machine Learning", "AI", "Deep Learning"],
    "Software Engineering": ["Software Engineer", "Backend", "Frontend", "Full Stack", "Developer"],
    "Cloud & DevOps": ["Cloud", "DevOps", "Site Reliability", "SRE"],
    "Cybersecurity": ["Security", "Cyber", "Penetration Tester"],
    "Product & Project Management": ["Product Manager", "Project Manager"],
    "Business & Marketing": ["Marketing", "Sales", "Business Analyst"],
    "Other": []  # Default category for uncategorized roles
}

# Function to assign category
def categorize_job(title):
    if pd.isna(title):  # Handle missing values
        return "Other"
    for category, keywords in job_categories.items():
        if any(keyword.lower() in title.lower() for keyword in keywords):
            return category
    return "Other"

# Apply categorization using correct column name
df["Job Category"] = df["job_title"].astype(str).apply(categorize_job)

# Save the categorized data
df.to_csv("data/categorized_job_listings.csv", index=False)
print("Categorized job listings saved successfully!")
