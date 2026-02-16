# import scripts.extract_kaggle as kaggle
# import scripts.extract_google_trends as google_trends

# kaggle.extract()
# google_trends.extract()


# src/run_pipeline.py
from scripts.extract_api import extract_adzuna_jobs, save_adzuna_csv
from scripts.extract_dataset import load_kaggle_dataset
from scripts.extract_timeseries import extract_trends
from scripts.transform_clean import clean_adzuna_jobs, clean_kaggle_jobs, clean_google_trends
from scripts.visualize import plot_job_counts, plot_top_companies_adzuna, plot_salary_distribution, plot_job_counts_kaggle, plot_temporal_analysis

# Extract
adzuna_data = extract_adzuna_jobs(pages=2)
adzuna_df = save_adzuna_csv(adzuna_data)
kaggle_df = load_kaggle_dataset()

trends_df = extract_trends()

# # Transform & Clean
clean_adzuna = clean_adzuna_jobs()
clean_kaggle = clean_kaggle_jobs()
clean_google = clean_google_trends()


# # Visualize
# plot_trends()
plot_job_counts()
plot_top_companies_adzuna()
plot_salary_distribution()
plot_job_counts_kaggle()  
plot_temporal_analysis()