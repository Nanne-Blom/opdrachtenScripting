import math

def kubus_vol(zijde):
    return zijde ** 3

def bol_vol(straal):
    return (4/3) * math.pi * (straal ** 3)

# Voorbeeld van het gebruik van de functies
kubus_zijde = 5
bol_straal = 4

kubus_volume = kubus_vol(kubus_zijde)
bol_volume = bol_vol(bol_straal)

print(f"De inhoud van deze kubus is: {kubus_volume}")
print(f"De inhoud van deze bol is: {bol_volume}")
