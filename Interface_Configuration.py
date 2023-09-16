import requests
import json

router = {
    "host": "Router_IP",
    "username": "username",
    "password": "Password",
    "port": "443"
}

# Step 1: Retrieve a list of all interfaces available on the router
url_interfaces = f"https://{router['host']}:{router['port']}/restconf/data/ietf-interfaces:interfaces"
headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
}

response_interfaces = requests.get(url_interfaces, headers=headers, auth=(router["username"], router["password"]), verify=False)

if response_interfaces.status_code != 200:
    print(f"Failed to retrieve interfaces. Status code: {response_interfaces.status_code}")
    exit()

interfaces_data = response_interfaces.json()["ietf-interfaces:interfaces"]["interface"]

# Create a numbered list of interfaces
interface_numbers = {}
for index, interface in enumerate(interfaces_data, start=1):
    interface_name = interface["name"]
    print(f"{index}- {interface_name}")
    interface_numbers[index] = interface_name

# Step 2: Allow the user to select an interface by number
while True:
    try:
        selected_interface_number = int(input("Enter the number of the interface to configure with an IP address: "))
        selected_interface_name = interface_numbers[selected_interface_number]
        break
    except (ValueError, KeyError):
        print("Invalid input. Please enter a valid number from the list.")

ip = input("Please Enter the IP to the Interface: ")
netmask = input("Please Enter the Netmask to the Interface: ")

# Construct the payload for configuring the selected interface
payload = json.dumps({
    "ietf-interfaces:interface": {
        "name": selected_interface_name,
        "description": "Configured by Luqman",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": ip,
                    "netmask": netmask
                }
            ]
        }
    }
})

# Configure the selected interface with an IP address and subnet mask
url_configure = f"https://{router['host']}:{router['port']}/restconf/data/ietf-interfaces:interfaces/interface={selected_interface_name}"
response_configure = requests.put(url_configure, headers=headers, data=payload, auth=(router["username"], router["password"]), verify=False)

if response_configure.status_code != 200:
    print(f"Failed to configure IP address. Status code: {response_configure.status_code}")
else:
    print(f"IP address {ip} with netmask {netmask} configured for interface {selected_interface_name}.")
