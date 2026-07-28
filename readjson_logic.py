import json

def find_stopped_servers(servers):
	stopped_servers = []
	for server in servers:
		if server["status"] == "stopped":
			stopped_servers.append(server["server_name"])
	return stopped_servers
