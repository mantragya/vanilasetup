import os
import requests
import json
from datetime import datetime,timezone
import logging
from src.logging_config import setup_logger


# GitHub API URL for listing user's gists
GITHUB_API_URL = 'https://api.github.com/users/{}/gists'

# File to store the last run timestamp
LAST_RUN_FILE = 'last_run.txt'

# Configure the logger using the setup_logger function
logger = setup_logger("github_gists", logging.INFO)

def fetch_user_gists(username,since=None):
    url = GITHUB_API_URL.format(username)
    params = {"since": since} if since else None
    response = requests.get(url,params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching gists: {response.status_code} - {response.text}")

#below functions are created to save multiple calls . But havent integrated in the main flow
def load_last_run_timestamp():
    if os.path.exists(LAST_RUN_FILE):
        with open(LAST_RUN_FILE, 'r') as file:
            timestamp_from_file = file.read()
            return timestamp_from_file.split(',')[1]
    else:
        return None

#below functions are created to save multiple calls . But havent integrated in the main flow
def save_last_run_timestamp(username,timestamp,file_path=LAST_RUN_FILE):
    with open(LAST_RUN_FILE, 'w') as file:
        file.write(username+","+str(timestamp))

#below functions are created to save multiple calls . But havent integrated in the main flow
def run_fetch_user_gists(username):
    if not username:
        logger.error("GitHub username is required.")
        return
    
    last_run_timestamp = load_last_run_timestamp() 

    # last_run_timestamp and username to fetch gists  
    gists = fetch_user_gists(username,last_run_timestamp)
    
    
    current_time = datetime.now(timezone.utc).isoformat()

    if last_run_timestamp:
        logger.info(f"Gists created or updated since the last run ({last_run_timestamp}):")
    else:
        logger.info("User's publicly available gists:")

       
    for gist in gists:
        created_at = gist["created_at"]
        print(f"{gist['description']} - {gist['html_url']} ({created_at})")
    
    save_last_run_timestamp(username,current_time)

def validate_username():
    username = os.environ.get("GITHUB_USERNAME","")
    if not username:
        return 
    else:
        return username


if __name__ == '__main__':
    username = validate_username() 
    run_fetch_user_gists("mantragya")
