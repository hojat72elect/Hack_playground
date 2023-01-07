import requests

from src.socket import penetration_targets

http_prefix = "http://"

get_request = requests.get(http_prefix + penetration_targets.makarem_shirazi)
for field, value in get_request.headers.items():
    print(field + ": " + value)
