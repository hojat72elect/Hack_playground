import requests
from src.socket import penetration_targets

http_prefix = "http://"

first_website_available_options: requests.Response = requests.options(http_prefix + penetration_targets.komite_emdad)
if first_website_available_options.status_code == 504:
    print("The server is really slow, can't contact it.")

# When a server is very slow, you will get HTTP 504 error.

# Another HTTP options request to a faster server
second_website_available_options: requests.Response = requests.options(http_prefix + penetration_targets.khamenei1)
print(second_website_available_options)
print(second_website_available_options.headers)
print(second_website_available_options.url)
print(second_website_available_options.content)
print(second_website_available_options.cookies)
