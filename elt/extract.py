import requests
import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv('API_URL')

# connect to API and extract data
def extract_data():
    response = requests.get(URL)
    response.raise_for_status() # catch API errors
    return response.json()['PublicAssistanceFundedProjectsDetails']
