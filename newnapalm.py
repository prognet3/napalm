# from napalm import get_network_driver
# listdevices = ['192.168.55.4', '192.168.55.5']
# for i in listdevices:
#     var1 = get_network_driver('ios')
#     var2 = var1(hostname=i, username="cisco", password="cisco")
#     var2.open()
#     var3 = var2.get_users()
#     print(var3)
#     print(type(var3))


#ip scp server enable
from napalm import get_network_driver

var1 = get_network_driver('ios')
var2 = var1(hostname="192.168.55.4", username="cisco", password="cisco")
var2.open()

var2.load_merge_candidate(filename='./aclconfig.cfg')
var2.commit_config()

