import json
with open('/Users/nuraiaitbazar/Desktop/pp2/Lab4/sample_data.json', 'r') as file:
    data = json.load(file)

output = {
    "totalcount": str (len(data['imdata'])),
    'imdata': []
}

for item in data['imdata']:
    li_phys_if = item ['l1PhysIf']['attributes']

format_interface = "{:<50} {:<80} {:<30}".format(
    li_phys_if ['adminSt'],
    li_phys_if ['bw'],
    li_phys_if ['mode']
)

print(format_interface)
print("="*80)
print(f"total count {output['totalcount']}")