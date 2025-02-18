import json

with open("/Users/madikbaizakov/Documents/vscode/PP2/lab4/sample-data.json", "r") as file:



    data = json.load(file)

interfaces = data["imdata"]

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print("-" * 80)

for interface in interfaces:
    attributes = interface["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes.get("descr", "")
    speed = attributes.get("speed", "inherit")
    mtu = attributes.get("mtu", "")
    print(f"{dn:<50} {descr:<20} {speed:<7} {mtu:<6}")
