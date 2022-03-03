import requests
import json

url = "https://api.github.com/users/anjaligarala/repos"
token = "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"
headers = {"Authorization": f"token {token}"}

response = requests.get(url)
data_json = json.loads(response.text)

for elem_dict in data_json:
    print(elem_dict['name'])
