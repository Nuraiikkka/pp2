sample_json_data = {
  "interfaces": [
    {
      "dn": "topology/pod-1/node-201/sys/phys-[eth1/33]",
      "description": "",
      "speed": "inherit",
      "mtu": 9150
    },
    {
      "dn": "topology/pod-1/node-201/sys/phys-[eth1/34]",
      "description": "",
      "speed": "inherit",
      "mtu": 9150
    },
    {
      "dn": "topology/pod-1/node-201/sys/phys-[eth1/35]",
      "description": "",
      "speed": "inherit",
      "mtu": 9150
    }
  ]
}

header = f"{'DN':<50} {'Description':<20} {'Speed':<6} {'MTU':<4}"
separator = "=" * 80

print("Interface Status")
print(separator)
print(header)
print("-" * len(header))

for interface in sample_json_data["interfaces"]:
    dn = interface["dn"]
    description = interface["description"]
    speed = interface["speed"]
    mtu = interface["mtu"]
    print(f"{dn:<50} {description:<20} {speed:<6} {mtu:<4}")
