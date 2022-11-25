from requests import get

"""
What exactly this service of hacker target API does?

hacker target API is limited and has quotas.
"""

host = 'www.leader.ir'
lookup = 'https://api.hackertarget.com/reverseiplookup/?q=%s' % host

# Send a get request with this website to the hacker target API
try:
    reverse_ip_lookup_result = get(lookup).text
    print(reverse_ip_lookup_result)
except Exception as e:
    print("error occurred while contacting the website ", str(e))
