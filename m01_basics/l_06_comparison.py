#!/usr/bin/env python
from util.create_utils import create_devices
from pprint import pprint
from random import randint, uniform
from datetime import datetime

devices = create_devices(num_subnets=2, num_devices=10)
print("\n NAME      VENDOR : OS   IP ADDRESS    VERSION")
print("   ------      ------   --   ----------    -------")

for device in devices:
    print(
        f'{device["name"]:>7} {device["vendor"]:>10}: {device["os"]:<6} {device["ip"]:<10} {device["version"]:>10}'
)


print("\n NAME      VENDOR : OS   IP ADDRESS    VERSION")
print(" ------      ------   --   ----------    -------")
for device in devices:
    if device["vendor"].lower() != "cisco":
        print(f'{device["name"]:>7} {device["vendor"]:>10}: {device["os"]:<6} {device["ip"]:<10} {device["version"]:>10}')

print("\n-------- Start comparison of device name ---------")
for index, device_a in enumerate(devices):
    for device_b in devices[index+1:]:
        if device_a["name"] == device_b["name"]:
            print(
                f"Found match! {device_a['name']} for both {device_a['ip']} and {device_b['ip']}"
)
print("---- Comparison of device names completed ----")


print("\n------ Create table of arbitrary 'standard' versions for each vendor:os -----")
standard_versions = dict()
for device in devices:
    vendor_os = device['vendor'] + ":" + device['os']
    if vendor_os not in standard_versions:
        standard_versions[vendor_os] = device['version']
pprint(standard_versions)

print("\n----- Create list of non-compliant device OS versions for each vendors:os -----")
non_compliant_devices=dict()
for vendor_os, _ in standard_versions.items():
    non_compliant_devices[vendor_os] = []

print(non_compliant_devices)
for device in devices:
    vendor_os = device['vendor'] + ":" + device['os']
    if device['version'] != standard_versions[vendor_os]:
        non_compliant_devices[vendor_os].append(device["ip"] + " version:" + device['version'])

pprint(non_compliant_devices)

print("\n\n----- Assesment, copy, and deep copy ---------------")
devices2 = devices
devices[0]["name"] = "this is a dumb device name"
if devices2 == devices:
    print("\n Assignment and modification: devices2 STILL equals devices")
    print("  --->moral Assignment is NOT the same as copy!")
else:
    print("   huh?")

from copy import copy
from copy import deepcopy

devices2 = copy(devices)
devices2[0]["name"] = "this is a dumb device name"
if devices2 == devices:
    print("\n copy: devices2 STILL equals devices")
else:
    print("   huh?")

devices2 = deepcopy(devices)
devices2[0]["name"] = "this is a dumb device name"
if devices2 == devices:
    print("\n copy: devices2 STILL equals devices")
else:
    print("   huh?")


