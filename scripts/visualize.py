# src/visualize.py
# src/visualize.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set a clean style for all seaborn plots
sns.set(style="whitegrid")

def plot_job_counts(file_path="data/cleaned/adzuna_jobs_cleaned.csv"):
    """
    Plot top 10 locations with the most AI job openings.
    
    Arguments:
    file_path : str : path to cleaned Adzuna jobs CSV file
    
    Saves plot to data/processed/job_locations_plot.png
    """
    # Check file existence
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    # Load cleaned Adzuna jobs
    df = pd.read_csv(file_path)

    # Count job openings by location and get top 10
    top_locations = df['location'].value_counts().head(10)

    # Create bar plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_locations.values, y=top_locations.index, palette="viridis")
    plt.title("Top 10 Locations with AI Job Openings", fontsize=14)
    plt.xlabel("Number of Jobs", fontsize=12)
    plt.ylabel("Location", fontsize=12)

    # Ensure output folder exists
    os.makedirs("images", exist_ok=True)

    # Save plot
    plt.savefig("images/job_locations_plot.png", bbox_inches='tight')
    # plt.show()
    print("Job locations plot saved to data/processed/job_locations_plot.png")


def plot_top_companies_adzuna(file_path="data/cleaned/adzuna_jobs_cleaned.csv"):
    """
    Plot top 10 companies hiring for AI roles.
    
    Arguments:
    file_path : str : path to cleaned Adzuna jobs CSV file
    
    Saves plot to data/processed/top_companies_plot.png
    """
    # Check file existence
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    # Load cleaned data
    df = pd.read_csv(file_path)

    # Count jobs by company and get top 10
    top_companies = df['company'].value_counts().head(10)

    # Create horizontal bar plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_companies.values, y=top_companies.index, palette="magma")
    plt.title("Top 10 Companies Hiring for AI Roles", fontsize=14)
    plt.xlabel("Number of Jobs", fontsize=12)
    plt.ylabel("Company", fontsize=12)

    # Ensure output folder exists
    os.makedirs("images", exist_ok=True)

    # Save plot
    plt.savefig("images/top_companies_plot.png", bbox_inches='tight')
    # plt.show()
    print("Top companies plot saved to images/top_companies_plot.png")


def plot_salary_distribution(file_path="data/cleaned/adzuna_jobs_cleaned.csv"):
    """
    Plot salary distribution (minimum and maximum) for AI job openings.
    
    Arguments:
    file_path : str : path to cleaned Adzuna jobs CSV file
    
            Saves plot to data/processed/salary_distribution_plot.png
    """
    # Check file existence
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    # Load cleaned data
    df = pd.read_csv(file_path)

    # Filter out jobs without salary info
    df = df[(df['salary_min'] > 0) & (df['salary_max'] > 0)]

    # Plot salary distributions
    plt.figure(figsize=(12, 6))
    sns.histplot(df['salary_min'], color='blue', label='Min Salary', kde=True, bins=30)
    sns.histplot(df['salary_max'], color='green', label='Max Salary', kde=True, bins=30)
    plt.title("Salary Distribution for AI Jobs", fontsize=14)
    plt.xlabel("Salary", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    plt.legend()

    # Ensure output folder exists
    os.makedirs("images", exist_ok=True)

    # Save plot
    plt.savefig("images/salary_distribution_plot.png", bbox_inches='tight')
    # plt.show()
    print("Salary distribution plot saved to data/processed/salary_distribution_plot.png")

def plot_job_counts_kaggle(file_path="data/cleaned/ai_jobs_kaggle_cleaned.csv"):
    df = pd.read_csv(file_path)
    top_locations = df['Job_Title'].value_counts().head(10)
    sns.barplot(x=top_locations.values, y=top_locations.index)
    plt.title("Top 10 Job Titles")
    plt.xlabel("Number of Jobs")
    plt.ylabel("Job Title")
    plt.savefig("images/job_counts_kaggle.png")
    # plt.show()
    print("Job counts plot saved to images/job_counts_kaggle.png")

def plot_temporal_analysis(file_path="data/cleaned/ai_google_trends_cleaned.csv"):
    google_df = pd.read_csv(file_path)
    plt.figure(figsize=(10, 6))
    for column in google_df.columns[1:]:
        plt.plot(google_df['date'], google_df[column], label=column)
    plt.title('Temporal Analysis of AI Interest Over Time')
    plt.xlabel('Date')
    plt.ylabel('Interest Over Time')
    plt.legend()
    plt.savefig("images/temporal_analysis.png")







