names = ["anay", "anu", "vinu", "vinayak", "chimnu"]
persons = [{"name": "anu", "location": "pune", "handsome": True, "intelligent": "maybe"},
           {"name": "vinu", "location": "indore", "handsome": False, "intelligent": "maybenot"},
           {"name": "anay", "location": "sfo", "handsome": True, "intelligent": "maybe"}]

for name in names:
    print(f"the current name is: {name}")

for person in persons:
    print(f"the current person is: {person}")
