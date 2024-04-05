from ncclient import manager

import xml.dom.minidom

m = manager.connect (
    host="192.168.1.1",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
    )

netconf_filter = """
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
"""

netconf_reply = m.get_config(source="running", filter=('subtree', netconf_filter))
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

