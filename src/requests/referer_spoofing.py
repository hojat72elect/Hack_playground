import requests

from src.socket import penetration_targets

# we write the desired header data into a dictionary
headers = {'Referer ': 'http://www.peter-lustig.com'}
http_prefix = "http://"

# give that header to the web server as part of our GET request
get_response = requests.get(http_prefix + penetration_targets.makarem_shirazi, data=headers)

print(type(get_response))
print(get_response.content)
