import os

#Adzuna API credentials
#setting as env variable for security
ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID")
ADZUNA_APP_KEY = os.getenv("ADZUNA_APP_KEY")

COUNTRY="us"
KEYWORD="artificial intelligence"
RESULTS_PER_PAGE=50
MAX_PAGES=3  #number of pages to extract

# Set environment variables
os.environ["ADZUNA_APP_ID"] = "31b863f3"
os.environ["ADZUNA_APP_KEY"] = "1b2755b89a2d8632255239af7c7a0cf2"