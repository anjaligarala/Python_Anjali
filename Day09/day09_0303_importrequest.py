import requests
import json

# response = requests.get("https://api.github.com/users/anjaligarala")
# print(response.cookies)

# from requests.auth import HTTPBasicAuth
# response = requests.get("https://api.github.com / users. ", auth=HTTPBasicAuth('anjaligarala', 'anjegarala15'))

# token for GITHUB API--> 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


url = "https://api.github.com/user/repos"
token = "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"
headers = {"Authorization": f"token {token}"}
repository_name = input("Enter your repos name:")
data = {"name": f"{repository_name}"}
username = input("Enter your username:")
url_delete = f"https://api.github.com/repos/{username}/{repository_name}"

# API to create new repo in Git
# requests.post(url, data=json.dumps(data), headers=headers)

# API to delete repo
# requests.delete(url_delete, headers=headers)
