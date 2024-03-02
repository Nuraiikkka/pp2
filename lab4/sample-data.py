import json
with open('/Users/nuraiaitbazar/Desktop/pp2/Lab4/sample-data.json', 'r') as file:
    data = json.load(file)

print("{:<50} {:<25} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("=" * 95)

for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']
    format_interface = "{:<50} {:<25} {:<10} {:<10}".format(
        attributes.get('dn', ''),
        attributes.get('descr', ''),
        attributes.get('speed', ''),
        attributes.get('mtu', '')
    )
    print(format_interface)

print("=" * 95)
print(f"Total count: {len(data['imdata'])}")


