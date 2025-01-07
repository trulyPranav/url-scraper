import requests
from bs4 import BeautifulSoup

def check_keywords_in_url(url, keywords):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f"Error fetching the URL: {e}"
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    page_text = soup.get_text().lower()

    for keyword in keywords:
        if keyword.lower() in page_text:
            print(f"Keyword '{keyword}' found in the URL.") 
        elif keyword.lower() not in page_text:
            print(f"Keyword '{keyword}' not found in the URL")
        else:
            print("None of the keywords found in the URL.")

url = "https://mec.tinkerhub.org"
keywords = ["community", "tinkhack", "TinkerHub", "notTinkerHub"]
check_keywords_in_url(url, keywords)