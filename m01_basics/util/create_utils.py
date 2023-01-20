#!/usr/bin/env python
from random import choice
import string


def create_devices(num_devices=1, num_subnets=1):
    """
    Create faker devices.

    try it out
    """
    created_devices = []

    if num_devices > 254 or num_subnets > 254:
        print("Error: too many devices and/or subnets requested")
        return created_devices

    for subnet_index in range(1, num_subnets+1):

        for device_index in range(1, num_devices+1):

            device = {}

            device["name"] = (
                choice(["r2", "r3", "r4", "r6", "r10"])
                + choice(["L", "U"])
                + choice(string.ascii_letters)
            )

            device["vendor"] = choice(["juniper", "cisco", "arista"])

            if device["vendor"] == "cisco":
                device["os"] = choice(["ios", "iosxe", "nexus"])
                device["version"] = choice(["12.1(T).04", "14.07X", "8.12(S).010", "20.45"])
            elif device["vendor"] == "juniper":
                device["os"] = "junos"
                device["version"] = choice(["12.3R12-S15", "15.IR7-S6", "18.4R2-S3","15.1X53-D591"])
            elif device["vendor"] == "arista":
                device["os"] = "eos"
                device["version"] = choice(["4.24.1F", "4.23.2F", "4.22.1F", "4.21.3F"])

            device["ip"] = "10.0" + str(subnet_index) + "." + str(subnet_index)

            created_devices.append(device)

    return created_devices


def create_network(num_devices=1, num_subnets=1):
    """
    Create a fake netoworks.

    try it
    """
    devices = create_devices(num_devices, num_subnets)
    network = dict()
    network["subnets"] = dict()

    for device in devices:
        subnet_address_bytes = device["ip"].split(".")
        subnet_address_bytes[3] = "0"
        subnet_address = ".".join(subnet_address_bytes)

        if subnet_address not in network["subents"]:
            network["subnets"][subnet_address] = dict()
            network["subnets"][subnet_address]["devices"] = list()

        network["subnets"][subnet_address]["devices"].append(device)

        interfaces = list()

        for index in range(0, choice([2, 4, 8])):
            interface = {
                "name": "g/0/0/" + str(index),
                "speed": choice(["10", "100", "1000"])
                }
            interfaces.append(interface)
        device["interfaces"] = interfaces

    return network
