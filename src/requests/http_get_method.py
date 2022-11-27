import requests
from src.socket import penetration_targets

# version of the library
print(requests.__version__)

'''
Making an HTTP GET request

The HTTP GET method requests a representation of the specified resource. 
Requests using GET should only be used to request data (they shouldn't 
include data). 

'''
result: requests.Response = requests.get(penetration_targets.isna)

print(result)  # The HTTP status of the result
print(result.text)  # HTML response
# HTTP 200 : Request has succeeded. A 200 response is cacheable by default.

# Now let's send 1000 requests and see how many of them will be accepted
for i in range(1, 11):
    batch_result = requests.get(penetration_targets.isna)
    print(i, "th request: ", batch_result)
