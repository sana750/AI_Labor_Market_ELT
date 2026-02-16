from pytrends.request import TrendReq
import pandas as pd
import os

def extract_trends(keywords=["Artificial Intelligence", "Deep Learning", "Data Scientist", "Data Analyst", "AI Engineer"], timeframe="2020-01-01 2026-01-01"):
    pytrends=TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(keywords, cat=0, timeframe=timeframe, geo='US', gprop='')
    data=pytrends.interest_over_time()
    data=data.drop(columns=['isPartial'])
    os.makedirs("data/processed", exist_ok=True)
    data.to_csv("data/processed/google_trends.csv")
    data.to_json("data/processed/google_trends.json", orient="records", indent=2)
    print(f"Google Trends data saved: {data.shape[0]} records")
    return data
