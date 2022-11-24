import socket
import ipaddress

"""
convert a website's address to IP address. 
"""

# The address of the website
website_address = 'www.leader.ir'

# The equivalent IP address of the website
input_ip_address: str = socket.gethostbyname(website_address)
print("Website's IP address is:", input_ip_address)

# Give it the str equivalent of the IP address. And will either get an IPv4 or IPv6
validated_ip = ipaddress.ip_address(input_ip_address)

# Is this IP local ?
print("Is this IP local ?", validated_ip.is_link_local)

# Is this IP global ?
print("Is this IP global ?", validated_ip.is_global)

print("What version is this IP ?", validated_ip.version)

# Let's see if this IP is referring to a network
validated_network = ipaddress.ip_network(input_ip_address)
print("The network behind this IP: ", validated_network)


