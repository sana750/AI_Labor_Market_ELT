# src/transform_clean.py
import pandas as pd
import os

def clean_adzuna_jobs(file_path="data/processed/adzuna_jobs.csv"):
    df = pd.read_csv(file_path)
    print(f"Initial shape: {df.shape}")

    # Remove duplicates
    df = df.drop_duplicates()
    # Fill missing values
    df['company'] = df['company'].fillna("Unknown")
    df['location'] = df['location'].fillna("Unknown")
    df['salary_min'] = df['salary_min'].fillna(0)
    df['salary_max'] = df['salary_max'].fillna(0)

    # Save cleaned data
    os.makedirs("data/cleaned", exist_ok=True)
    df.to_csv("data/cleaned/adzuna_jobs_cleaned.csv", index=False)
    df.to_json("data/cleaned/adzuna_jobs_cleaned.json", orient="records", indent=2)
    print(f"Cleaned Adzuna jobs saved: {df.shape}")
    return df

def clean_kaggle_jobs(file_path="data/processed/ai_jobs_kaggle.csv"):
    kaggle_df = pd.read_csv(file_path)
    print("Data Quality Assessment for Kaggle dataset:")
    kaggle_missing_values=kaggle_df.isnull().sum()
    kaggle_duplicate_records=kaggle_df.duplicated().sum()
    kaggle_unique_values=kaggle_df.nunique()
    print("Number of missing values in kaggle datasets:", kaggle_missing_values)
    print("Number of duplicate records in kaggle datasets:", kaggle_duplicate_records)
    print("Number of unique values in kaggle datasets:", kaggle_unique_values)

    #(b) Transformation and Cleaning:
    #Kaggle dataset transformation and cleaning:
    print("Kaggle transformation and cleaning:")

    kaggle_df=kaggle_df.drop_duplicates() #removing duplicates
    kaggle_df['Salary_USD']=pd.to_numeric(kaggle_df['Salary_USD'], errors='coerce') #converting salary to numeric
    median_salary=kaggle_df['Salary_USD'].median()
    kaggle_df['Salary_USD']=kaggle_df['Salary_USD'].fillna(median_salary)


    #normalizing text columns
    text_columns=['Job_Title', 'Industry', 'Company_Size', 'Location', 'AI_Adoption_Level', 'Automation_Risk', 'Required_Skills', 'Remote_Friendly', 'Job_Growth_Projection']
    for column in text_columns:
        kaggle_df[column]=kaggle_df[column].str.lower()
        kaggle_df[column]=kaggle_df[column].str.strip()

    print("Kaggle dataset summary statistics:", kaggle_df.describe())

    kaggle_df.to_csv("data/cleaned/ai_jobs_kaggle_cleaned.csv", index=False)
    kaggle_df.to_json("data/cleaned/ai_jobs_kaggle_cleaned.json", orient="records", indent=2)
    print(f"Cleaned Kaggle jobs saved: {kaggle_df.shape}")
    return kaggle_df


def clean_google_trends(file_path="data/processed/google_trends.csv"):
    google_df = pd.read_csv(file_path)
    print("Data Quality Assessment for Google dataset:")
    google_missing_values=google_df.isnull().sum()
    google_duplicate_records=google_df.duplicated().sum()
    google_unique_values=google_df.nunique()   
    print("Number of missing values in google datasets:", google_missing_values)
    print("Number of duplicate records in google datasets:", google_duplicate_records)
    print("Number of unique values in google datasets:", google_unique_values)

    #Google dataset transformation and cleaning
    print("Google transformation and cleaning:")
    google_df=google_df.drop_duplicates() #removing duplicates
    google_df=google_df.fillna(0) #filling missing values with 0
    google_df['date']=pd.to_datetime(google_df['date']) #converting date to datetime

    print("Google dataset summary statistics:", google_df.describe())

    #saving google cleaned dataset
    google_df.to_csv("data/cleaned/ai_google_trends_cleaned.csv", index=False)
    google_df.to_parquet("data/cleaned/ai_google_trends_cleaned.parquet")
    print(f"Cleaned Google trends saved: {google_df.shape}")
    return google_df

