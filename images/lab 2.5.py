# Jesse Sillman ITMI22SP

import requests
requests.packages.urllib3.disable_warnings()  # Disable SSL warnings

# RESTCONF API URL for the Loopback99 interface
api_url = "https://192.168.1.1/restconf/data/ietf-interfaces:interfaces/interface=Loopback99"

# Headers for accepting YANG-data+json
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

# HTTP Basic Authentication
basicauth = ("cisco", "cisco123!")

# Sending the DELETE request to remove the interface configuration
resp = requests.delete(api_url, auth=basicauth, headers=headers, verify=False)

# Checking and printing the response
if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: Interface deleted successfully with status code {}".format(resp.status_code))
else:
    print("Error code {}, reply: {}".format(resp.status_code, resp.text))
