import requests
from bs4 import BeautifulSoup

class X:
    @staticmethod
    def get_X_Username(username):
        url = f'https://twitter.com/{username}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        if "No results found" not in soup.text:
            print(f"User '{username}' exists on X."
                  f"\nURL: {url}")
        else:
            print(f"User '{username}' does not exist.")