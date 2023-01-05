from pprint import pprint

#Dictionary representing a device

device = {
    "name": "sbx-n9kv-ao",
    "vendor": "cisco",
    "model": "Nexus9000 C9308v Chassis",
    "os": "nxos",
    "version": "9.3(3)",
    "ip": "10.1.1.1",
}

# SIMPLE PRINT
print("\n_____ SIMPLE PRINT _____________")
print("device:",  device)
print("device name: ", device["name"])

# PRETTY PRINT
print("\n_____ PRETTY PRINT __________")
pprint(device)

# FOR LOOP, NICELY FORMATTED PRINT

print("\n_____ FOR LOOP, USING F-STRING __________")
for key, value in device.items():
    print(f"{key:>16s} : {value}")
