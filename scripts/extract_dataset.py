import pandas as pd
import os

def load_kaggle_dataset(file_path="data/raw/ai_job_market_insights.csv"):
    df=pd.read_csv(file_path)
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/ai_jobs_kaggle.csv", index=False)
    df.to_json("data/processed/ai_jobs_kaggle.json", orient="records", indent=2)
    print(f"Kaggle dataset loaded: {df.shape[0]} records")
    return df
