import json

with open("shodan_data.json", 'r+') as file:
    lines = file.readlines()
    result = []
    for line in lines:
        data = json.loads(line)
        result.append(data)
    addresses = ["http://" + camera['ip_str'] + ":" + str(camera['port']) for camera in result]
    with open("addresses.json", 'w+') as addr_file:
        addr_file.write(json.dumps(addresses))