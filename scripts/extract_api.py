import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

def extract_adzuna_jobs(keyword="artificial intelligence", country="us", pages=3, results_per_page=50):
    all_jobs=[]
    for page in range(1, pages + 1):
        url=f"https://api.adzuna.com/v1/api/jobs/{country}/search/{page}"
        params={
            "app_id": APP_ID,
            "app_key": APP_KEY,
            "what": keyword,
            "results_per_page": results_per_page,
            "content-type": "application/json"
        }
        response=requests.get(url, params=params)
        if response.status_code == 200:
            data=response.json()
            jobs=data.get("results", [])
            all_jobs.extend(jobs)
            print(f"Page {page}: {len(jobs)} jobs extracted")
        else:
            print(f"Error {response.status_code} on page {page}")
            break

    #saving raw into JSON
    os.makedirs("data/raw", exist_ok=True)
    with open("data/raw/adzuna_jobs.json", "w", encoding="utf-8") as f:
        json.dump(all_jobs, f, indent=2, ensure_ascii=False)
    print(f"Total jobs extracted: {len(all_jobs)}")
    return all_jobs

#converting to CSV
import pandas as pd

def save_adzuna_csv(all_jobs):
    rows=[]
    for job in all_jobs:
        rows.append({
            "title": job.get("title"),
            "company": job.get("company", {}).get("display_name"),
            "location": job.get("location", {}).get("display_name"),
            "description": job.get("description"),
            "salary_min": job.get("salary_min"),
            "salary_max": job.get("salary_max"),
            "redirect_url": job.get("redirect_url")
        })
    df=pd.DataFrame(rows)
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/adzuna_jobs.csv", index=False)
    df.to_json("data/processed/adzuna_jobs.json", orient="records", indent=2)
    print("Saved processed Adzuna jobs CSV and JSON")
    return df
