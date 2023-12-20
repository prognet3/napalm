# import yaml
#
# with open("yamlfile.yml") as nameyaml:
#     var1 = yaml.load(nameyaml, Loader=yaml.SafeLoader)
# print(var1)
# print(type(var1))
#
#
# with open("yamlfile.yml") as y:
#     var2 = yaml.safe_load(y)
# print(var2)
import yaml
from jinja2 import Environment, FileSystemLoader

var1 = Environment(loader=FileSystemLoader('.'))
template = var1.get_template('template.j2')

with open("yamlfile.yml") as y:
    var2 = yaml.safe_load(y)

var3 = template.render(data={'var10': var2})
print(var3)
