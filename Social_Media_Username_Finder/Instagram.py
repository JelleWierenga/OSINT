import requests
from bs4 import BeautifulSoup

class Instagram:
    @staticmethod
    def get_Instagram_Username(username):
        url = f'https://www.instagram.com/{username}/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        if "No results found" not in soup.text:
            print(f"User '{username}' exists on Instagram."
                  f"\nURL: {url}")
        else:
            print(f"User '{username}' does not exist.")