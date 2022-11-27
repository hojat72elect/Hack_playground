import requests
from src.socket import penetration_targets

"""
The HTTP HEAD method requests the headers that would be returned if the HEAD request's URL was instead 
requested with the HTTP GET method. For example, if a URL might produce a large download, a HEAD request 
could read its Content-Length header to check the filesize without actually downloading the file.

As you can see below, the header will give lots of important info about the HTTP server.

"""

http_result: requests.Response = requests.head(" http://" + penetration_targets.makarem_shirazi)
result_dictionary = dict(http_result.headers)
print(result_dictionary)
print("HTTP server: ", result_dictionary['Server'])
print("Cache-Control: ", result_dictionary['Cache-Control'])
print("Content-Encoding: ", result_dictionary['Content-Encoding'])
