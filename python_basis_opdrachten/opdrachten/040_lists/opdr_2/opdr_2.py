rivier_info = { 
    "rijn": ["nederland", "duitsland", "Frankrijk"], 
    "maas": ["nederland", "belgië", "duitsland"], 
    "nijl": ["egypte", "soedan", "oeganda"] 
}

rivieren = list(rivier_info.keys())


rivier = rivieren[0]

land = rivier_info[rivier][1]

print(f"De rivier {rivier.capitalize()} stroomt onder andere door {land.capitalize()}")

rivier = rivieren[1]

land = rivier_info[rivier][0]

print(f"De rivier {rivier.capitalize()} stroomt onder andere door {land.capitalize()}")

rivier = rivieren[2]

land = rivier_info[rivier][2]

print(f"De rivier {rivier.capitalize()} stroomt onder andere door {land.capitalize()}")
