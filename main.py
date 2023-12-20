from jinja2 import Template
from netmiko import ConnectHandler
# jinja_file = "jinja2file.j2"
variable_jinja = {
    "hostname": "router1",
    "ntp1": "5.4.3.2",
    "ntp2": "6.5.4.3",
    "route": "7.6.5.4",
    "access_list": [
        {
            "remark": "user1",
            "acl": "10.10.10.0 0.0.0.255",
            "status": "down"
        },
        {
            "remark": "user2",
            "acl": "20.20.20.0 0.0.0.255",
            "status": "up"
        }

    ]
}

with open("jinja2file.j2", "r") as j2file:
    var1 = Template(j2file.read())
var2 = var1.render(variable_jinja)
print(var2)
var3 = var1.render(variable_jinja).splitlines()
print(var3)

connect_to_router = ConnectHandler(device_type="cisco_ios", host="192.168.50.153", username="test", password="test")
var1 = connect_to_router.send_config_set(var3)
