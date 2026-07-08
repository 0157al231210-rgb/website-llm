import requests

def download(url):
    try:
        response = requests.get(url, timeout=10)  # Set a timeout for the request
    
        if response.status_code == 200:
            return response.text
    
    except requests.RequestException as e:
        return None