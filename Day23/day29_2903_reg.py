import re

server_names = ["studio-server", "licence", "licence-server1", "filesync-server-2", "filesync-ser", "licence-ser-2",
                "ad-server", "admirror-server", "ad-server2", "ad--server-2"]

regex_pattern = "ad-.+"

for server_name in server_names:
    if re.search(regex_pattern, server_name):
        print(server_name)
