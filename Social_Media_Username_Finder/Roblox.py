import requests
from bs4 import BeautifulSoup

username = 'TommySoBored'

class Roblox:
    @staticmethod
    def get_Roblox_Username(username):
        url = f'https://www.roblox.com/search/users?keyword={username}&startIndex=0'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        if "No results found" not in soup.text:
            print(f"User '{username}' exists."
                  f"\nURL: {url}")
        else:
            print(f"User '{username}' does not exist.")
