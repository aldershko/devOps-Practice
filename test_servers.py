import json
from readjson_logic import find_stopped_servers

def test_find_stopped_servers():
    servers = [
        {"server_name": "web-01", "status": "running"},
        {"server_name": "db-01", "status": "stopped"},
    ]
    result = find_stopped_servers(servers)
    assert result == ["db-01"], f"Expected ['db-01'], got {result}"

test_find_stopped_servers()
print("Test passed")
