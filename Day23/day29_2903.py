import re

tenant_project_name = "pts-sre-sohil-2"
filesync_url = "https://filesync-server-1-pts-sre-sohil-2.platform.cloud.slb-ds.com/login"

regex_pattern = f'^https://(.+?)-{tenant_project_name}'

print(re.search(regex_pattern, filesync_url).group(1))
