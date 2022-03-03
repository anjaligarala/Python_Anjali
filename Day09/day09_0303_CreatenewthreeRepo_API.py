import requests
import json

url = "https://api.github.com/user/repos"
token = "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"
headers = {"Authorization": f"token {token}"}
url_list = "https://api.github.com/users/repos"

for repo_name in range(2):
    repository_name = input("Enter your repos name:")
    data = {"name": f"{repository_name}"}
    requests.post(url, data=json.dumps(data), headers=headers)
