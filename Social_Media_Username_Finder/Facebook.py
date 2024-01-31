# import requests
# from bs4 import BeautifulSoup
#
# class Facebook:
#     @staticmethod
#     def get_Facebook_Username(username):
#         for i in range(10):
#             url = f'https://www.facebook.com/{username}.{i}'
#             response = requests.get(url)
#             soup = BeautifulSoup(response.text, 'html.parser')
#             if "No results found" not in soup.text:
#                 print(f"User '{username}' exists on Facebook."
#                       f"\nURL: {url}")
#             else:
#                 print(f"User '{username}' does not exist.")

import requests
import json

with open('config.json') as config_file:
    config = json.load(config_file)
    access_token = config.get('fb_access_token')

user_id = '100011345588929'

url = f'https://graph.facebook.com/{user_id}?fields=id,name&access_token={access_token}'

response = requests.get(url)
data = response.json()

print(data)