#!/usr/bin/env python
from pprint import pprint

device1_str = " r3-L-n7, cisco, catalyst 2960, ios "

# SPLIT
print("STRING STRIP, SPLIT, REPLACE")
device1 = device1_str.split(",")
print("device using split:")
print("  ", device1)

# STRIP
device1 = device1_str.strip(" ").split(",")
print("device 1 using strip and split")
print("  ", device1)

# REMOVE BLANKS
device1 = device1_str.replace(" ", "").split(",")
print("device1 replaced blanks using split:\n ", device1)


# REMOVE BLANKS, CHANGES COMMA TO COLON 
device1_str_colon = device1_str.replace(" ", "").replace(",", ":")
print("device1 replaced blanks comma to colon:")
print(" ", device1_str_colon)

# LOOP WITH STRIP AND SPLIT
device1 = list()
for item in device1_str.split():
    device1.append(item.strip())
print("device1 using loop and strip for each item: ")
print(" ", device1)

# STRIP AND SPLIT, SINGLE LINE USING LIST COMPREHENSION
device1 = [item.strip() for item in device1_str.split(",")]
print("device1 using list comprehension")
print(" ", device1)

# IGNORING CASE
print("\n\nIFNORING CASE")
model = "CSR1000V"
if model.lower() == "csr1000v":
    print(f"matched using lower(): {model}")
else:
    print(f"didn't match : {model}")

# FINDING SUBSTRING
print("\n\nFINDING SUBSTRING")
version = "Virtual XE Software, Version1.1"
expected_version = "Version1.1"
index = version.find(excepted_version)
if index > 0:
    print(f"Found version: {excepted_version} at location {index}")
else:
    print(f"not found: {expected_version}")






