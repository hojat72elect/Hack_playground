import requests
from src.socket import penetration_targets

"""
The HTTP HEAD method requests the headers that would be returned if the HEAD request's URL was instead 
requested with the HTTP GET method. For example, if a URL might produce a large download, a HEAD request 
could read its Content-Length header to check the filesize without actually downloading the file.

As you can see below, the header will give lots of important info about the HTTP server.
"""
http_prefix = "http://"

header_first: requests.Response = requests.head(http_prefix + penetration_targets.makarem_shirazi)
result_dictionary_first = dict(header_first.headers)
print(result_dictionary_first)
print("HTTP server: ", result_dictionary_first['Server'])
print("Cache-Control: ", result_dictionary_first['Cache-Control'])
print("Content-Encoding: ", result_dictionary_first['Content-Encoding'])

# Let's get the header of another target and compare that with this one:
header_second: requests.Response = requests.head(http_prefix + penetration_targets.irna)
result_dictionary_second = dict(header_second.headers)
print(result_dictionary_second)
