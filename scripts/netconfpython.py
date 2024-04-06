from ncclient import manager
import xml.dom.minidom

m = manager.connect (
    host="192.168.1.1",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
    )

print("#Supported Capabilities (YANG models):")
for capability in m.server_capabilities:
 print(capability)
