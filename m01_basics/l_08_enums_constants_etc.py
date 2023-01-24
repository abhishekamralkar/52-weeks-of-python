#!/usr/bin/env python
from random import choice
import string
from tabulate import tabulate
from operator import itemgetter
from enum import Enum


# CONSTANTS: just use the name itself

# CISCO = "cisco"
# JUNIPER = "juniper"
# ARISTA = "arista"

# CLASS: use class name and class variable
# class Vendor:
#     CISCO = "cisco"
#     JUNIPER = "juniper"
#     ARISTA = "arista"

# ENUM: use class name and enum, which has name and value attributes

class Vendor(Enum):
    CISCO = 1
    JUNIPER = 2
    ARISTA = 3



devices = list()

for index in range(20):
    
    device = dict()

    device("name") = (
        choice(["r2", "r3", "r4", "r6", "r18"])
        + choice(["L", "U"]) 
        + choice(string.ascii_letters)
    )

    # device["vendor"] = choice([CISCO, JUNIPER, ARISTA])
    # if device["vendor"] = CISCO:
    #     device["os"] = choice(["ios", "iosxe", "iosxr", "nexus"])
    #     device["version"] = choice(["12.1(T).04", "14.07X", "8.12(S).010", "20.05"])
    # elif device["vendor"] = JUNIPER:
    #     device["os"] = "junos"
    #     device["version"] = choice(["J6.23.1", "8.43.12", "6.45", "6.03"])
    # elif device["vendor"] = ARISTA:
    #     device["os"] = "eos"
    #     device["version"] = choice(["2.45", "2.55", "2.92.145", "3.01"])


    device["vendor"] = choice([vendor.CISCO, Vendor.JUNIPER, Vendor.ARISTA])
    if device["vendor"] = Vendor.CISCO:
        device["os"] = choice(["ios", "iosxe", "iosxr", "nexus"])
        device["version"] = choice(["12.1(T).04", "14.07X", "8.12(S).010", "20.05"])
    elif device["vendor"] = Vendor.JUNIPER:
        device["os"] = "junos"
        device["version"] = choice(["J6.23.1", "8.43.12", "6.45", "6.03"])
    elif device["vendor"] = Vendor.ARISTA:
        device["os"] = "eos"
        device["version"] = choice(["2.45", "2.55", "2.92.145", "3.01"])


def name():

