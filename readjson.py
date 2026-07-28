import json

with open("server_config.json", "r") as file:
	data = json.load(file)
stopped_servers = []
for server in data:
	if server["status"] == "stopped":
		stopped_servers.append(server["server_name"])
print("Stopped servers:", stopped_servers)
