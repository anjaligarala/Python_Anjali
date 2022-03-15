# create new repo using function

import requests
import json


# url = "https://api.github.com/user/repos"
# token = "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"
# headers = {"Authorization": f"token {token}"}

def create_repo_github(create_url, token, repository_name, list_repo_url):
    for repo_name in range(1):
        data = {"name": f"{repository_name}"}
        response = requests.post(create_url, data=json.dumps(data), headers={"Authorization": f"token {token}"})
        print(response.status_code)

    response = requests.get(list_repo_url)  # get the github url
    data_json = json.loads(response.text)  #

    for elem_dict in data_json:
        if elem_dict['name'] == repository_name:
            return "Repo you created is present - " + elem_dict['name']

    return "Repo not present"


a = create_repo_github("https://api.github.com/user/repos", "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",
                       "Day20_CreateRepo_Function", "https://api.github.com/users/anjaligarala/repos")
print(a)
