# Workforce Demand and Hiring Trend Analysis

## 📌 Project Overview
This project analyzes workforce demand and hiring trends using real-world datasets. The goal is to gain insights into job market trends, hiring patterns, and demand for specific skills across industries.

## 📂 Project Structure
```
Workforce-Demand-Analysis/
│-- data/              # Stores datasets (CSV, JSON, etc.)
│-- notebooks/         # Jupyter notebooks for analysis
│-- scripts/           # Python scripts for data processing
│-- reports/           # Generated reports and insights
│-- docs/              # Documentation and references
│-- README.md          # Project documentation
│-- requirements.txt   # Required Python libraries
│-- .gitignore         # Files to exclude from Git
│-- LICENSE            # Project license
```

## 🛠️ Setting Up the Environment

### **1️⃣ Create a Virtual Environment**
Before installing dependencies, set up a virtual environment:
```sh
python -m venv venv
```

### **2️⃣ Activate the Virtual Environment**
**For Windows:**
```sh
venv\Scripts\activate
```
**For Mac/Linux:**
```sh
source venv/bin/activate
```

### **3️⃣ Installing Libraries**
To install the necessary dependencies:
```sh
pip install -r requirements.txt
```

## 📌 How to Add Only Selected Libraries to `requirements.txt`
If you don’t want to include all installed libraries, use:
```sh
pip freeze > all_packages.txt  # Save all installed packages
```
Then, filter and create `requirements.txt` with only the necessary packages:
```sh
pip freeze | findstr /R "pandas numpy matplotlib seaborn scikit-learn requests" > requirements.txt
```
To install from this file later:
```sh
pip install -r requirements.txt
```

```

---

## 📊 Data Loading & Exploration

### **1️⃣ Dataset Used:**
- **Glassdoor Data Science Jobs - 2024** (Downloaded from Kaggle)

### **2️⃣ Loading the Dataset**
- **Script Name:** `load_explore_data.py`
- **Location:** `scripts/`

#### **Code to Load CSV:**
```python
import pandas as pd

# Load dataset
file_path = "data/glassdoor_ds_jobs_2024.csv"  # Adjust filename if needed
df = pd.read_csv(file_path)

# Display first few rows
print(df.head())
```

### **3️⃣ Checking Column Names**
```python
print("\n📌 Column Names in Dataset:")
print(df.columns)
```

### **4️⃣ Fixing KeyError Issue**
Column names are case-sensitive. The correct column name is `"job_title"`, not `"Job Title"`.

```python
print(df["job_title"].unique()[:10])  # Display first 10 unique job titles
```

### Handling Missing Values

#### 1️⃣ Check Missing Values
```sh
python scripts/handle_missing_values.py
```
- Prints missing values in each column.

#### 2️⃣ Handling Missing Values (Basic Approach)
```sh
python scripts/clean_missing_values_basic.py
```
- Fills numerical missing values with mean.
- Fills categorical missing values with most frequent value.

#### 3️⃣ Handling Missing Values (Advanced Approach)
```sh
python scripts/clean_missing_values_predict.py
```
- Uses **sklearn SimpleImputer** to handle missing values.
- Converts salary data to numeric before imputation.
- Fixes `inplace=True` warnings by using direct assignment instead.

### File Paths & Execution Notes
- **With `pathlib` (Recommended):**
  ```python
  from pathlib import Path
  file_path = Path("data/glassdoor_jobs.csv")
  df = pd.read_csv(file_path)
  ```
- **Without `pathlib` (Alternative):**
  ```python
  file_path = "data/glassdoor_jobs.csv"
  df = pd.read_csv(file_path)
  ```
- **Ensure you run scripts from the root directory:**
  ```sh
  python scripts/your_script.py
  ```

  ### 5️⃣ Exploratory Data Analysis (EDA)
```sh
python scripts/exploratory_data_analysis.py
```
- Generates descriptive statistics.
- Visualizes distributions of key variables.
- Creates a correlation matrix heatmap.
- Saves output visualizations in the `images/` directory.

## Summary of EDA Findings
- **Salary distribution:** Most salaries are concentrated in a specific range, with some outliers.
- **Company ratings:** Most companies have ratings between 3 and 4.
- **Employment types:** Majority of jobs are full-time, with fewer part-time or contract positions.
- **Industry trends:** Certain industries dominate job postings, indicating high demand.
- **Correlation analysis:** Identified relationships between salary, company size, and other factors.

## File Paths & Execution Notes
- **With `pathlib` (Recommended):**
  ```python
  from pathlib import Path
  file_path = Path("data/glassdoor_jobs.csv")
  df = pd.read_csv(file_path)
  ```
- **Without `pathlib` (Alternative):**
  ```python
  file_path = "data/glassdoor_jobs.csv"
  df = pd.read_csv(file_path)
  ```
- **Ensure you run scripts from the root directory:**
  ```sh
  python scripts/your_script.py
  ```

## Final Cleaned Dataset
The cleaned dataset is saved as:
```
data/glassdoor_jobs_cleaned_final.csv
```

## 📌 Job Title Normalization

### 🔹 Why Normalize Job Titles?
Job titles can vary widely across companies, making it difficult to analyze workforce demand effectively. Normalization helps by:
- **Standardizing Job Titles:** Converts similar job titles (e.g., "Sr. Data Scientist" and "Senior Data Scientist") into a common format.
- **Reducing Redundancy:** Eliminates variations caused by abbreviations, seniority levels, or special characters.
- **Improving Analysis:** Ensures better grouping and comparison of job roles across different organizations.

### 🛠 How Was It Done?
- **Text Cleaning:** Job titles were converted to lowercase and stripped of unnecessary characters.
- **Standardization Rules:** Common patterns (e.g., "Sr." → "Senior", "ML Engineer" → "Machine Learning Engineer") were applied.
- **Output Generation:** A new column, **`normalized_job_title`**, was created to store the cleaned and standardized job titles.

### 📂 Generated Output
- The normalized job data is saved in **`normalized_job_listings.csv`** for further processing.


## 📌 Job Role Categorization

### 🔹 Why Categorize Job Roles?
Categorizing job roles helps in:
- **Understanding Workforce Trends:** Identifying the demand for specific job categories like Data Science, Software Engineering, and Cloud & DevOps.
- **Comparing Hiring Patterns:** Analyzing which industries are hiring the most for certain roles.
- **Salary Insights:** Grouping job roles helps in comparing salary trends across different categories.
- **Better Visualization:** Categorized data allows for clearer insights when creating visualizations and dashboards.

### 🛠 How Was It Done?
- A mapping was created where specific **keywords** (e.g., "Data Scientist", "AI", "Cloud") were assigned to relevant job categories.
- The script scans **job titles** and assigns them to predefined **categories**.
- Jobs that do not match any category are classified under **"Other"**.

### 📂 Generated Output
- The categorized data is saved in **`categorized_job_listings.csv`** for further analysis.

## 📊 Exploratory Data Analysis (EDA) – Job Demand Analysis  

### 🔹 Why Conduct EDA?  
Exploratory Data Analysis (EDA) helps us understand the job market trends and hiring patterns by analyzing key metrics. It provides valuable insights into:  

- **Most In-Demand Job Roles** – Identifying roles with the highest demand.  
- **Industry Hiring Trends** – Understanding which industries are growing the fastest.  
- **Salary Distribution** – Analyzing salary estimates across different job categories.  
- **Location-Based Hiring Trends** – Identifying regions with high job availability.  

### 🛠 Steps Taken  
1. **Data Cleaning & Preprocessing**  
   - Handled missing values and standardized job titles.  
2. **Visualization of Job Demand**  
   - Created bar charts to show the most frequently posted job roles.  
   - Analyzed job openings across different industries.  
3. **Salary Trends Analysis**  
   - Plotted salary distributions for various job roles.  
4. **Regional Hiring Analysis**  
   - Identified cities and states with the highest job postings.  

### 📈 Key Insights  
- **High demand for tech-related roles**, including **Data Science, Software Engineering, and Cloud Computing**.  
- The **"Other" category had a significant market presence**, indicating a diverse job market.  
- Certain **industries showed rapid growth**, highlighting future job opportunities.  

### 📁 Output File  
The findings from this EDA are saved as:  

# 📊 Job Demand Analysis  

## 🔍 Overview  
This step analyzes job demand across different **industries** and **sectors** based on job listing data. We visualize the **top 10 industries** and **top 10 sectors** with the highest number of job postings.  

## 📌 Key Steps  
1. **Loaded categorized job listings** from `categorized_job_listings.csv`.  
2. **Counted job listings** for each industry and sector.  
3. **Plotted bar charts** for the top 10 industries and sectors.  
4. **Saved analysis results** as CSV files:  
   - `industry_demand_analysis.csv`  
   - `sector_demand_analysis.csv`  
5. **Exported visualizations** as PNG files:  
   - `industry_demand.png`  
   - `sector_demand.png`  

## 📊 Visualizations  
### 🔹 **Top 10 Industries by Job Demand**  
<img src="industry_demand.png" alt="Industry Demand" width="600">

### 🔹 **Top 10 Sectors by Job Demand**  
<img src="sector_demand.png" alt="Sector Demand" width="600">

## 🚀 Next Steps  
Proceeding with further **job trend analysis**, **salary insights**, and **location-based demand** analysis.  
