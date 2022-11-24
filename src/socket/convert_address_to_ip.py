import socket

"""
convert a website's address to IP address. 
"""

# The address of the website
website_address = 'www.leader.ir'

# The IP address of the website
ip_address: str = socket.gethostbyname(website_address)
print("Website's IP address:", ip_address)
