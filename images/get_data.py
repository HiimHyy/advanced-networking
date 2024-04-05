from ncclient import manager

import xmltodict

m = manager.connect (
    host="192.168.1.1",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
    )

netconf_reply = m.get(filter=("xpath", "/interfaces-state/interface"))
netconf_reply_dict = xmltodict.parse(netconf_reply.xml)
for interface in netconf_reply_dict["rpc-reply"]["data"]["interfaces-state"]["interface"]:
 print("Name: {} MAC: {} Input: {} Output {}".format(
 interface["name"],
 interface["phys-address"],
 interface["statistics"]["in-octets"],
 interface["statistics"]["out-octets"]
 )
 )
