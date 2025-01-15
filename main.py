from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

def check_keywords_in_url(url, keywords):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f"Error fetching the URL: {e}"

    soup = BeautifulSoup(response.content, 'html.parser')
    page_text = soup.get_text().lower()

    result = {}
    for keyword in keywords:
        if keyword.lower() in page_text:
            result[keyword] = "found"
        else:
            result[keyword] = "not found"
    
    return result

@app.route('/check_keywords', methods=['POST'])
def check_keywords():
    data = request.get_json()  # Get the incoming JSON data
    if not data or 'url' not in data or 'keywords' not in data:
        return jsonify({'error': 'URL and keywords are required'}), 400

    url = data['url']
    keywords = data['keywords']
    
    # Call the check_keywords_in_url function
    result = check_keywords_in_url(url, keywords)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
